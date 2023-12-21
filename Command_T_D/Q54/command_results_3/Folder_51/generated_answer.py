def all_right_truncatable_prime(n):
    result = []
    for x in range(2, n[54] + 1):
        if x % 2 == 0:
            continue
        if all(x % y == 0 for y in range(3, int(str(x)[-1]))) and x != 1:
            continue
        result.append(x)
    return result
