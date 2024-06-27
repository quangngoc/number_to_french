from typing import Iterator
import argparse

french_words = [
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
numbers = list(range(1, 17)) + [20, 30, 40, 50, 60]
number_to_french_dict = {number: word for number, word in zip(numbers, french_words)}


def less_than_20_to_french(tens: int, remainder: int) -> Iterator[str]:
    """Convert numbers less than 20 into French words."""
    if tens > 1:
        # Won't handle the case where number > 19
        return
    elif tens == 1 and remainder > 6:
        # Numbers in [17, 18, 19].
        yield from ["dix", number_to_french_dict[remainder]]
    elif tens != 0 or remainder != 0:
        # Numbers between 1 and 10.
        yield number_to_french_dict[tens * 10 + remainder]


def number_to_french(number: int) -> Iterator[str]:
    """Convert a number to French."""
    if number >= 10**6:
        raise ValueError("Number is too big")
    if number == 0:
        yield "zéro"
        return

    # Handle thousands.
    (thousands, remainder) = divmod(number, 1000)
    if thousands > 0:
        if thousands > 1:
            yield from number_to_french(thousands)
        if thousands > 1 and remainder == 0:
            yield "milles"
        else:
            yield "mille"
        if remainder == 1:
            yield "et"

    # Handle hundreds.
    (hundreds, remainder) = divmod(remainder, 100)
    if hundreds > 0:
        if hundreds > 1:
            yield number_to_french_dict[hundreds]
        if hundreds > 1 and remainder == 0:
            yield "cents"
        else:
            yield "cent"
        if remainder == 1:
            yield "et"

    # Handle less than 100.
    (tens, remainder) = divmod(remainder, 10)
    if tens > 7:
        yield "quatre-vingts" if tens == 8 and remainder == 0 else "quatre-vingt"
        yield from less_than_20_to_french(tens - 8, remainder)
    elif tens > 5:
        yield "soixante"
        if remainder == 1:
            yield "et"
        yield from less_than_20_to_french(tens - 6, remainder)
    elif tens > 1:
        yield number_to_french_dict[tens * 10]
        if remainder == 1:
            yield "et"
        if remainder > 0:
            yield number_to_french_dict[remainder]
    else:
        yield from less_than_20_to_french(tens, remainder)


def number_to_french_text(number: int) -> str:
    return "-".join(list(number_to_french(number)))


def main():
    parser = argparse.ArgumentParser(description="Convert numbers to French words")
    parser.add_argument(
        "numbers", nargs="+", type=int, help="List of numbers to convert"
    )
    args = parser.parse_args()

    french_numbers = [number_to_french_text(n) for n in args.numbers]
    for num, french in zip(args.numbers, french_numbers):
        print(f"{num}: {french}")


if __name__ == "__main__":
    main()
