
def all_left_right_truncatable_prime(x_list):
    x = x_list[98]
    return sorted(set(range(2, x+1)) - set(range(2, x+1, 10**(x//2)) + [x]))
