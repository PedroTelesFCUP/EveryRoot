# References and attribution

EveryRoot builds on established work in reinforcement learning and search. The research proposal concerns their specific integration in the implemented chess-learning flow. It makes no first-in-field claim for PPO, SAC, self-play, imitation learning or learning from search.

| Work | Relevance to EveryRoot |
| --- | --- |
| Schulman et al. (2017), [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | Clipped policy-update objective; EveryRoot uses it with a direct local search reward |
| Haarnoja et al. (2018), [Soft Actor-Critic](https://arxiv.org/abs/1801.01290) | Separate off-policy actor-critic learner for compute allocation |
| Haarnoja et al. (2018), [Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905) | SAC implementation background, including automatic entropy adjustment |
| Anthony, Tian and Barber (2017), [Thinking Fast and Slow with Deep Learning and Tree Search](https://arxiv.org/abs/1705.08439) | Expert Iteration and the precedent for learning to generalise search decisions |
| Silver et al. (2017), [Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/abs/1712.01815) | AlphaZero's combination of self-play, neural learning and tree search |
| Leela Chess Zero contributors, [Technical Explanation of Leela Chess Zero](https://lczero.org/dev/wiki/technical-explanation-of-leela-chess-zero/) | Contemporary policy/value-guided chess search; architectural context |
| Stockfish contributors, [official engine repository](https://github.com/official-stockfish/Stockfish) and [time management source](https://github.com/official-stockfish/Stockfish/blob/master/src/timeman.cpp) | Engine context and direct attribution for the allocation teacher's copied equations |

The EveryRoot source records Stockfish revision `47be34c55fbc86079cba57b9ad6955e6fe0bdff9` for its allocation-teacher equations. That identifier is reported from implementation provenance. The linked default-branch source can change. Stockfish's [GPLv3 licence](https://github.com/official-stockfish/Stockfish/blob/master/Copying.txt) and upstream authorship must be respected in any subsequent source release; the document's rights notice does not override them.

Bibliographic entries are provided in [references.bib](references.bib). The report explains where these methods are used and where EveryRoot differs.
