
def all_left_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: is_left_right_truncatable_prime(x), range(3, n[0] + 1))))

def is_left_right_truncatable_prime(x):
    return all(x % 2 == 0 or x % 2 == 1 for x in range(x, 1, -1)) and x != 1 and x != 2
