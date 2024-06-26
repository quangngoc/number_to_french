import pytest
from number_to_french.number_to_french import less_than_20_to_french


@pytest.mark.parametrize(
    "tens, remainder, expected_output",
    [
        (0, 5, ["cinq"]),
        (1, 6, ["seize"]),
        (1, 8, ["dix", "huit"]),
    ],
)
def test_less_than_20_to_french(tens, remainder, expected_output):
    result = list(less_than_20_to_french(tens, remainder))
    assert result == expected_output
