import pytest
from number_to_french.number_to_french import less_than_20_to_french, number_to_french

numbers_in_french = {
    0: "zéro",
    1: "un",
    5: "cinq",
    10: "dix",
    11: "onze",
    15: "quinze",
    20: "vingt",
    21: "vingt-et-un",
    30: "trente",
    35: "trente-cinq",
    50: "cinquante",
    51: "cinquante-et-un",
    68: "soixante-huit",
    70: "soixante-dix",
    71: "soixante-et-onze",
    75: "soixante-quinze",
    99: "quatre-vingt-dix-neuf",
    100: "cent",
    101: "cent-et-un",
    105: "cent-cinq",
    111: "cent-onze",
    123: "cent-vingt-trois",
    168: "cent-soixante-huit",
    171: "cent-soixante-et-onze",
    175: "cent-soixante-quinze",
    199: "cent-quatre-vingt-dix-neuf",
    200: "deux-cents",
    201: "deux-cent-et-un",
    555: "cinq-cent-cinquante-cinq",
    999: "neuf-cent-quatre-vingt-dix-neuf",
    1000: "mille",
    1001: "mille-et-un",
    1111: "mille-cent-onze",
    1199: "mille-cent-quatre-vingt-dix-neuf",
    1234: "mille-deux-cent-trente-quatre",
    1999: "mille-neuf-cent-quatre-vingt-dix-neuf",
    2000: "deux-milles",
    2001: "deux-mille-et-un",
    2020: "deux-mille-vingt",
    2021: "deux-mille-vingt-et-un",
    2345: "deux-mille-trois-cent-quarante-cinq",
    9999: "neuf-mille-neuf-cent-quatre-vingt-dix-neuf",
    10000: "dix-milles",
    11111: "onze-mille-cent-onze",
    12345: "douze-mille-trois-cent-quarante-cinq",
    123456: "cent-vingt-trois-mille-quatre-cent-cinquante-six",
    654321: "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un",
    999999: "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf",
}


@pytest.mark.parametrize(
    "tens, remainder, expected_output",
    [
        (0, 5, ["cinq"]),
        (1, 6, ["seize"]),
        (1, 8, ["dix", "huit"]),
    ],
)
def test_less_than_20_to_french(tens: int, remainder: int, expected_output: list[str]):
    result = list(less_than_20_to_french(tens, remainder))

    # Assert
    assert result == expected_output


@pytest.mark.parametrize("number", numbers_in_french.keys())
def test_number_to_french_less_than_million(number: int):
    result = list(number_to_french(number))

    # Assert
    words = [word for element in result for word in element.split("-")]
    assert words == numbers_in_french[number].split("-")


@pytest.mark.parametrize("number", [1000000, 1000001])
def test_number_to_french_greater_than_million(number: int):
    with pytest.raises(ValueError, match="Number is too big"):
        _ = list(number_to_french(number))
