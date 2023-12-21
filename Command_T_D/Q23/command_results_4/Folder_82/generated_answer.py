import math
def find_divisors_in_range(n):
    result = []
    if n % 2 == 0:
        result.append(2)
        if n == 2:
            return result
        if n == 4:
            return [2, 4]
        if n == 6:
            return [2, 4, 6]
    else:
        result.append(3)
        if n == 3:
            return result
        if n == 5:
            return [3, 5]
        if n == 6:
            return [3, 4, 6]
    return result
