# Number to french converter

Number can be hard to write in French.

[https://fr.wikipedia.org/wiki/Nombres_en_français](https://fr.wikipedia.org/wiki/Nombres_en_fran%C3%A7ais)

## Setup

```bash
py -3.9 -m venv .venv
& ./.venv/Scripts/Activate.ps1
```

## Development

```bash
pip install build pytest pytest-cov pytest-sugar
pytest ./tests --cov=src
py -m build
```

## Run

```bash
pip install -e .
number-to-french 42 71 192
```

## Tools used

- VsCode
- [Codeium](https://codeium.com)
- ChatGPT for helping writh unit tests:

```text
Write the following french words for the following number [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
Return a dictionary with key is the number and value if french words.
All french word should use a dash "-", for example: vingt-et-un.
```
