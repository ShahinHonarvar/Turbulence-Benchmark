
def if_decimal_is_divisible(binary_repr: str) -> bool:
    fibonacci_sequence = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610)
    decimal_repr = int(binary_repr, 2)
    return (decimal_repr in fibonacci_sequence[37])
