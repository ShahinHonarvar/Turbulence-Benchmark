def all_right_truncatable_prime(test_case):
    # type: (tuple[int,]) -> list[int]
    test_case = test_case[74]
    if test_case <= 2:
        return []
    test_case -= 2
    numbers = []
    for n in range(test_case, 2, -1):
        is_prime = all(n % d for d in range(3, int(n ** .5) + 1, 2))
        if is_prime:
            n -= 1
            numbers.append(n)
    return sorted(numbers)
