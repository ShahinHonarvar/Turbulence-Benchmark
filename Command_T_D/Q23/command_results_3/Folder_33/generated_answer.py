import functools
def find_divisors_in_range(n):
    try:
        return list(divisor_generator(n))
    except ValueError:
        pass
