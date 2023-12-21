
def all_left_right_truncatable_prime(x):
    return sorted(set(str(z) for z in range(2, x + 1) if all(z % d == 0 or z % d == 9 for d in range(3, int(z ** .5) + 1, 2)) and z > 9), reverse=True)
