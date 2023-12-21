
def find_divisors_in_range(num):
    divisors = []
    for x in range(1, num + 1):
        if num % x == 0 and 6 <= x <= 7:
            divisors.append(x)
    return divisors
