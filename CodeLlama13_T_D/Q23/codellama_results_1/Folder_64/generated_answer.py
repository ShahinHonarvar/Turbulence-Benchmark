
def find_divisors_in_range(num):
    divisors = []
    for i in range(1, 10):
        if num % i == 0 and i <= 9:
            divisors.append(i)
    return divisors
