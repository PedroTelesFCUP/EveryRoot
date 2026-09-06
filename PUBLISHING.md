# Publishing EveryRoot on GitHub and Zenodo

This package presents the EveryRoot architecture, its research contribution and the intended chess product. The engine source code and trained weights are excluded. Nothing in this package has been uploaded or published, and no DOI has been reserved.

The publication title is **EveryRoot: Learning Chess Moves and Search Allocation**, by **Pedro Teles**.

## The release

Use GitHub for the project page and Zenodo for a permanent, citable copy of the architecture report and its supporting documentation. Deposit the following together in **one Zenodo record**, with the resource type **Publication → Report**:

- `report/EveryRoot_Architecture_Report.pdf`
- `EveryRoot_GitHub_Zenodo.zip`, the matching documentation package

The JSON file at `metadata/zenodo_fields.json` supplies the text to enter in the Zenodo form. It is a preparation aid, not an API request. The report's 2026 document year is not a claim that publication has already occurred.

## GitHub

1. Create a repository for the reviewed documentation package. It can remain private while the release is being prepared.
2. Upload the contents of this package, preserving the folder structure. The README is the project page; the PDF is the architecture report.
3. Use the existing `CITATION.cff` and `RIGHTS.md`. Do not select an automatic MIT, Apache or Creative Commons licence when creating the repository.
4. Once the real repository address exists, add it to the report and publication metadata. Use an immutable release link for the archived documentation version.

GitHub uses `CITATION.cff` to display a citation box. This file uses `preferred-citation: type: report` so the public documentation is cited as a report. [GitHub citation documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files).

## Zenodo

1. Create a new upload draft. Select **Publication → Report**, enter the title, author and description from `metadata/zenodo_fields.json`, and use the actual publication date when releasing it.
2. Review the rights entry. Zenodo defaults to **CC-BY 4.0**; this package instead prepares an **all rights reserved** notice. If that is the author's final choice, remove the default licence, choose **Add custom**, and enter the title and description supplied in the metadata file. [Zenodo licences and rights](https://help.zenodo.org/docs/deposit/describe-records/licenses/).
3. Under DOI, answer **No** to an existing DOI and choose **Get a DOI now!**. This reserves an actual identifier in the draft. Copy it into the report, README and the `preferred-citation` section of `CITATION.cff`. [Zenodo DOI reservation](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/).
4. Rebuild the PDF and ZIP with the reserved DOI and consistent release metadata, then upload both files to that same draft. Add the real GitHub release address as a related link.
5. Review the final files, author details and rights together. Publish the approved GitHub release and Zenodo record, and verify that the DOI resolves to the intended files.

The current preparation deliberately leaves the DOI, repository address, ORCID, affiliation and publication date unset. Enter those only when confirmed. A reserved DOI becomes registered through publication; a placeholder in a local file does not reserve one.

## Keep the archive straightforward

This release uses a manual report deposit. Leave GitHub-to-Zenodo automatic software archiving disabled for it, avoiding a second DOI for the same report bundle. [Zenodo resource types](https://help.zenodo.org/docs/deposit/describe-records/resource-type/).

There is no active `.zenodo.json` in the package. If one is introduced later, Zenodo gives it precedence over `CITATION.cff` when importing GitHub release metadata. Licence handling can ultimately fall back to Zenodo's default if no recognised licence is supplied, so an omitted licence is not a substitute for an explicit rights choice. [Metadata precedence](https://help.zenodo.org/docs/github/describe-software/zenodo-json/), [GitHub import licence handling](https://support.zenodo.org/help/en-gb/24-github-integration/149-how-to-specify-a-license-for-a-software-record-on-github).

A DOI makes this architectural description citable and records its publication. The deposited report should be described as a research disclosure; the DOI does not establish exclusive rights to the underlying ideas.
