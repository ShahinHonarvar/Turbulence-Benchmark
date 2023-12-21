def find_divisors_in_range(n):
    x = [1, 2, 3, 5, 6, 7, 11, 12, 17, 19, 23, 29, 31, 37, 41, 43]
    return [i for i in range(27, 44) if n % i == 0]
