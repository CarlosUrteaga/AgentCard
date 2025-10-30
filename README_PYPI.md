# agentcard

A lightweight Python library to define, validate, and document **AI agents** using the *Agent Card* specification.

## Installation
```bash
pip install agentcard
```

## Quick usage
```python
from agentcard import AgentCard
card = AgentCard.from_yaml("example.yaml")
card.register_to_phoenix()
```

## License
**BibTeX**
```bibtex
@inproceedings{urteaga2025agentcards,
  author    = {Urteaga-Reyesvera, J. Carlos and Lopez Murphy, Juan Jose},
  title     = {Agent Cards: A Documentation Standard for Operational AI Agents},
  booktitle = {Proceedings of the MICAI 2025 Workshops},
  series    = {Lecture Notes in Artificial Intelligence},
  publisher = {Springer Nature Switzerland AG},
  note      = {Forthcoming},
  year      = {2025},
  url       = {https://github.com/CarlosUrteaga/AgentCard}
}

