# Number to french converter

Number can be hard to write in French.

[https://fr.wikipedia.org/wiki/Nombres_en_français](https://fr.wikipedia.org/wiki/Nombres_en_fran%C3%A7ais)

## Development

```bash
py -3.9 -m venv .venv
& ./.venv/Scripts/Activate.ps1
pip install build pytest pytest-cov pytest-sugar
pytest ./tests --cov=src
py -m build
```
