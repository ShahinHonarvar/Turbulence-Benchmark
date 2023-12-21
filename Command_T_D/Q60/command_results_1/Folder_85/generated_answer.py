
def all_left_right_truncatable_prime(x):
    return sorted(set(range(2, x + 1)) for i in range(x) if i == int(str(i)[0] + str(i)[-1]))
