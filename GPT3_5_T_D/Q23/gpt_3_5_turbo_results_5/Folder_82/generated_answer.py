
def find_divisors_in_range(num):
    divisors = []
    for i in range(4, 7):
        if num % i == 0:
            divisors.append(i)
    return divisors
