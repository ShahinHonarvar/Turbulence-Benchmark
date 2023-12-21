
def all_left_right_truncatable_prime(x):
    if x <= 3:
        return []
    x -= 2
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            continue
        if x % i == i:
            continue
        if all(int(d) for d in str(x // i)):
            return [x // i]
    return []
