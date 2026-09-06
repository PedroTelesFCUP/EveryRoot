"""Rebuild the architecture figure and PDF from the included Markdown.

Run from any directory: python scripts/build_publication.py
Dependencies: matplotlib, reportlab; DejaVu Sans fonts available on this system.
This script runs no chess searches, training or games.
"""
from pathlib import Path
import html
import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path as MplPath
from matplotlib import font_manager
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / 'figures'
REPORT = ROOT / 'report'
FIG.mkdir(exist_ok=True)
REPORT.mkdir(exist_ok=True)
NAVY = '#142C42'
TEAL = '#13766B'
BLUE = '#315F9C'
AMBER = '#A56818'
INK = '#243746'
GREY = '#647684'


def build_figure():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none'})
    fig, ax = plt.subplots(figsize=(12, 7.1))
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    def box(x, y, w, h, title, desc, color, fill):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008,rounding_size=0.014',
                                   linewidth=1.3,edgecolor=color,facecolor=fill))
        ax.text(x+w/2,y+h*.69,title,ha='center',va='center',fontsize=13,fontweight='bold',color=color)
        ax.text(x+w/2,y+h*.30,desc,ha='center',va='center',fontsize=11.4,color=INK,linespacing=1.25)
    def arrow(points, color=GREY):
        p=MplPath(points, [MplPath.MOVETO]+[MplPath.LINETO]*(len(points)-1))
        ax.add_patch(FancyArrowPatch(path=p,arrowstyle='-|>',mutation_scale=15,
                                    linewidth=1.8,facecolor=color,edgecolor=color))
    box(.05,.79,.27,.145,'PPO move policy','Chooses the played move',BLUE,'#EFF4FA')
    box(.385,.79,.26,.145,'Resulting position',"The opponent is to move",NAVY,'#F2F5F7')
    box(.385,.425,.26,.17,'Alpha-beta search','Adaptive depth\nand dynamic quiescence',NAVY,'#F2F5F7')
    box(.05,.425,.27,.17,'Move reward','Score minus pre-move Φ\nOriginal mover’s perspective',BLUE,'#EFF4FA')
    box(.385,.11,.26,.17,'Best-reply target','Cached at the searched root\nTeaches the next decision',BLUE,'#EFF4FA')
    box(.735,.79,.24,.145,'SAC allocator','Budget and STOP / MORE',TEAL,'#EDF7F3')
    box(.735,.425,.24,.17,'Sparse deeper audit','Evaluation error\nand node cost',TEAL,'#EDF7F3')
    arrow([(.325,.86),(.38,.86)])
    arrow([(.515,.78),(.515,.60)])
    ax.text(.53,.687,'Evaluate\nconsequences',fontsize=10.5,color=GREY,va='center',linespacing=1.3)
    arrow([(.38,.51),(.325,.51)],BLUE)
    arrow([(.185,.60),(.185,.785)],BLUE)
    ax.text(.203,.687,'Reinforcement learning',fontsize=10.5,color=BLUE,va='center')
    arrow([(.515,.42),(.515,.285)],BLUE)
    ax.text(.532,.35,'Reuse recommendation',fontsize=10.5,color=BLUE,va='center')
    arrow([(.38,.195),(.017,.195),(.017,.86),(.045,.86)],BLUE)
    ax.text(.18,.17,'Imitation learning',ha='center',va='top',fontsize=11,color=BLUE)
    arrow([(.755,.78),(.67,.69),(.642,.60)],TEAL)
    ax.text(.708,.69,'Controls search',fontsize=10.5,color=TEAL,ha='center',va='center',
            bbox=dict(facecolor='white',edgecolor='none',pad=2))
    arrow([(.65,.485),(.73,.485)],TEAL)
    arrow([(.858,.60),(.858,.785)],TEAL)
    ax.text(.88,.69,'SAC\nfeedback',fontsize=10.5,color=TEAL,ha='left',va='center')
    ax.text(.855,.29,'Audits train SAC.\nRecorded policy targets\nremain fixed.',ha='center',
            va='center',fontsize=11,color=TEAL,linespacing=1.5)
    ax.text(.51,.025,'One shared chess policy. A separate learner controls the cost of search.',
            ha='center',va='center',fontsize=12,color=NAVY,fontweight='bold')
    fig.subplots_adjust(left=.012,right=.988,top=.98,bottom=.02)
    fig.savefig(FIG/'learning_flow.png',dpi=220,facecolor='white')
    fig.savefig(FIG/'learning_flow.svg',facecolor='white')
    plt.close(fig)


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',
                  r'<link href="\2" color="#13766B">\1</link>', text)
    text = re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',text)
    text = re.sub(r'\*([^*]+)\*',r'<i>\1</i>',text)
    text = re.sub(r'`([^`]+)`',r'<font name="Mono">\1</font>',text)
    return text


def build_pdf():
    for face, prop in [('Body',font_manager.FontProperties(family='DejaVu Sans')),
                       ('BodyBold',font_manager.FontProperties(family='DejaVu Sans',weight='bold')),
                       ('BodyItalic',font_manager.FontProperties(family='DejaVu Sans',style='oblique')),
                       ('Mono',font_manager.FontProperties(family='DejaVu Sans Mono'))]:
        pdfmetrics.registerFont(TTFont(face,font_manager.findfont(prop)))
    pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='BodyItalic',boldItalic='BodyBold')
    styles={
      'body':ParagraphStyle('body',fontName='Body',fontSize=10.0,leading=14.9,textColor=HexColor(INK),spaceAfter=9),
      'h2':ParagraphStyle('h2',fontName='BodyBold',fontSize=21,leading=25.5,textColor=HexColor(NAVY),spaceAfter=17),
      'h3':ParagraphStyle('h3',fontName='BodyBold',fontSize=11.2,leading=15.3,textColor=HexColor(TEAL),spaceBefore=10,spaceAfter=7,keepWithNext=True),
      'quote':ParagraphStyle('quote',fontName='Body',fontSize=10.5,leading=17,textColor=HexColor(NAVY),backColor=HexColor('#EDF4F5'),borderPadding=11,spaceBefore=7,spaceAfter=17),
      'bullet':ParagraphStyle('bullet',fontName='Body',fontSize=10,leading=14.9,textColor=HexColor(INK),leftIndent=11,firstLineIndent=-8,spaceAfter=9),
      'caption':ParagraphStyle('caption',fontName='Body',fontSize=8.2,leading=11,textColor=HexColor(GREY),spaceAfter=11),
    }
    def page(c, doc):
        width,height=doc.pagesize
        c.saveState()
        c.setFillColor(HexColor(NAVY)); c.rect(0,height-10,width,10,fill=1,stroke=0)
        c.setFont('BodyBold',8); c.drawString(49,height-31,'EVERYROOT')
        c.setFont('Body',8); c.setFillColor(HexColor(GREY));c.drawRightString(width-49,height-31,'ARCHITECTURE RESEARCH NOTE')
        c.setStrokeColor(HexColor('#DCE5E9'));c.line(49,43,width-49,43)
        c.setFont('Body',8);c.drawString(49,29,'Pedro Teles  |  September 2026')
        c.drawRightString(width-49,29,str(doc.page))
        c.restoreState()
    story=[]
    lines=(ROOT/'docs/architecture_report.md').read_text().splitlines()
    para=[]
    def flush():
        if para:
            story.append(Paragraph(inline(' '.join(para)),styles['body']));para.clear()
    for line in lines:
        if line.startswith('# '):
            flush()
            story.append(Paragraph('EveryRoot',ParagraphStyle('title',fontName='BodyBold',fontSize=37,leading=43,textColor=HexColor(NAVY),spaceAfter=11)))
            story.append(Paragraph('Learning Chess Moves<br/>and Search Allocation',ParagraphStyle('subtitle',fontName='Body',fontSize=23,leading=29,textColor=HexColor(TEAL),spaceAfter=14)))
        elif line.startswith('Pedro Teles |'):
            story.append(Paragraph('Pedro Teles · Architecture research note · September 2026',styles['caption']))
        elif line=='<!-- pagebreak -->':
            flush();story.append(PageBreak())
        elif line.startswith('## '):
            flush();style=styles['h3'] if line.startswith('## 1.') else styles['h2']
            story.append(Paragraph(inline(line[3:]),style))
        elif line.startswith('### '):
            flush();story.append(Paragraph(inline(line[4:]),styles['h3']))
        elif line.startswith('!['):
            flush();story.append(Image(str(FIG/'learning_flow.png'),width=497,height=294.1));story.append(Spacer(1,9))
        elif line.startswith('> '):
            flush();story.append(Paragraph(inline(line[2:]),styles['quote']))
        elif line.startswith('- '):
            flush();story.append(Paragraph('• '+inline(line[2:]),styles['bullet']))
        elif not line.strip(): flush()
        else: para.append(line)
    flush()
    doc=SimpleDocTemplate(str(REPORT/'EveryRoot_Architecture_Report.pdf'),pagesize=(595.28,841.89),
                          rightMargin=49,leftMargin=49,topMargin=57,bottomMargin=57,
                          title='EveryRoot: Learning Chess Moves and Search Allocation',author='Pedro Teles',
                          subject='Architecture research note: local search rewards, search imitation and learned compute allocation')
    doc.build(story,onFirstPage=page,onLaterPages=page)


if __name__=='__main__':
    build_figure()
    build_pdf()
    print('Built figures/learning_flow.png, figures/learning_flow.svg and report/EveryRoot_Architecture_Report.pdf')
