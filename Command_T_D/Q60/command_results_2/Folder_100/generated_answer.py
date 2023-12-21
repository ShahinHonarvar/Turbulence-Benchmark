
def all_left_right_truncatable_prime(x_range):
    return [str(n) for n in range(2, x_range[1] + 1) if n % 2 == 1 and all(str(n)[-1] != "0" for n in range(2, int(str(n)[0]))) and all(str(n)[:1] != "0" for n in range(2, int(str(n)[0]))) and str(n) in str(2**10)]
