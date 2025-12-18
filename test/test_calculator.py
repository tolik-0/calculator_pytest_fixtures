import pytest
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    int_divide,
    modulo,
)


@pytest.fixture
def operands() -> tuple[int, int]:
    """Provide a reusable pair of integer operands."""
    # This pair is used in several tests as a common base case
    return 20, 5


@pytest.fixture
def zero_divisor() -> int:
    """Provide a reusable zero divisor."""
    return 0


def test_add_with_operands_fixture(operands: tuple[int, int]) -> None:
    """add() should return correct sum for fixture operands."""
    a, b = operands
    assert add(a, b) == 25


def test_subtract_with_operands_fixture(operands: tuple[int, int]) -> None:
    """subtract() should return correct difference for fixture operands."""
    a, b = operands
    assert subtract(a, b) == 15


def test_multiply_with_operands_fixture(operands: tuple[int, int]) -> None:
    """multiply() should return correct product for fixture operands."""
    a, b = operands
    assert multiply(a, b) == 100


def test_divide_with_operands_fixture(operands: tuple[int, int]) -> None:
    """divide() should return correct quotient for fixture operands."""
    a, b = operands
    assert divide(a, b) == 4.0


def test_int_divide_with_operands_fixture(operands: tuple[int, int]) -> None:
    """int_divide() should return correct integer quotient for fixture operands."""
    a, b = operands
    assert int_divide(a, b) == 4


def test_modulo_with_operands_fixture(operands: tuple[int, int]) -> None:
    """modulo() should return correct remainder for fixture operands."""
    a, b = operands
    assert modulo(a, b) == 0


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (2.5, 0.5, 3.0),
    ],
)
def test_add_parametrized(a: float, b: float, expected: float) -> None:
    """Parametrized test for add() with several pairs of operands."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 3, 1),
        (7, 7, 0),
        (25, 4, 1),
    ],
)
def test_modulo_parametrized(a: int, b: int, expected: int) -> None:
    """Parametrized test for modulo() with different integer pairs."""
    assert modulo(a, b) == expected


def test_divide_by_zero_raises(zero_divisor: int) -> None:
    """divide() should raise ZeroDivisionError when divisor is zero."""
    with pytest.raises(ZeroDivisionError):
        divide(10, zero_divisor)


def test_int_divide_by_zero_raises(zero_divisor: int) -> None:
    """int_divide() should raise ZeroDivisionError when divisor is zero."""
    with pytest.raises(ZeroDivisionError):
        int_divide(10, zero_divisor)


def test_modulo_by_zero_raises(zero_divisor: int) -> None:
    """modulo() should raise ZeroDivisionError when divisor is zero."""
    with pytest.raises(ZeroDivisionError):
        modulo(10, zero_divisor)
