from typing import Iterator

french_words = [
    "zéro",
    "un",
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "onze",
    "douze",
    "treize",
    "quatorze",
    "quinze",
    "seize",
    "vingt",
    "trente",
    "quarante",
    "cinquante",
    "soixante",
]
numbers = list(range(17)) + [20, 30, 40, 50, 60]
number_to_french_dict = {number: word for number, word in zip(numbers, french_words)}

def less_than_20_to_french(tens: int, remainder: int) -> Iterator[str]:
    if tens > 1:
        raise ValueError("Number too large")
    elif tens == 1 and remainder > 6:
        yield "dix"
        if remainder > 0:
            yield number_to_french_dict[remainder]
    elif tens != 0 or remainder != 0:
        yield number_to_french_dict[tens * 10 + remainder]