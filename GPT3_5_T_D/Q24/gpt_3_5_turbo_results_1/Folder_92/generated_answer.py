
def sum_of_divisors_in_range(num):
    divisors = [x for x in range(1, num // 2 + 1) if num % x == 0]
    result = sum([x for x in divisors if 8 <= x <= 9])
    return result if result != 0 else 0
