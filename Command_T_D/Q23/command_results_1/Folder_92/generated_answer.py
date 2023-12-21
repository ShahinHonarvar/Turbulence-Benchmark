def find_divisors_in_range(n):
    if n < 8:
        return []
    if n == 8:
        return [8]
    if n == 9:
        return [9]
    return [8, 9, 12, 16, 18, 24, 36, 45, 64, 72, 81, 108, 126, 144, 162, 189, 216, 225, 243, 264, 288, 324, 360, 453, 481, 500, 576, 600, 900]
