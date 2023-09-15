import pytest
from python_starter import evaluate


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("0", 0),
        # ("1 + 2", 3),
        # ("1 + 2", 3),
        # ("(1 + 2) * 5 / 2 + -3 * 7", -14)
    ],
)
def test_expression(expression: str, expected: int):
    # When the expression is evaluated
    result = evaluate(expression)

    # Then the result is as expected
    assert result == expected


# @pytest.mark.parametrize(
#     "expression",
#     (
#         "foo",
#     ),
# )
# def test_error(expression):
#     # Expect an error to be thrown when the expression is evaluated
#     with pytest.raises(ValueError):
#         evaluate(expression)
