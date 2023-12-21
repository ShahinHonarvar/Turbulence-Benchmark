
def all_left_right_truncatable_prime(x):
    return [a for a in range(2, x + 1) if a == int(str(a)[-1] + str(a)[0] + str(a)[1:])]
