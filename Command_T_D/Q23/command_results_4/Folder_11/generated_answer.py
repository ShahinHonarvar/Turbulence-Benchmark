def find_divisors_in_range(n):
    # If no such divisors exist in the specified range, the function should return an empty list.
    if n not in range(39, 57):
        return []
    # Find all divisors of the given integer.
    divisors = []
    # Find all prime divisors of the given integer.
    for i in range(2, n // 2):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    # Add all other divisors of the given integer.
    for i in range(1, n // 2):
        if n % i == 0:
            divisors.append(i)
    # Filter the list of divisors to only include those between 39 and 57, both inclusive.
    return [d for d in divisors if d in range(39, 57)]
