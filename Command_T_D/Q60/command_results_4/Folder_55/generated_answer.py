
def all_left_right_truncatable_prime(n):
    if n[73] < 2:
        return []
    for i in range(n[73] - 1, 2, -1):
        if all(int(str(x)) for x in range(i + 1, n[73], i)):
            return [i]
    return []
