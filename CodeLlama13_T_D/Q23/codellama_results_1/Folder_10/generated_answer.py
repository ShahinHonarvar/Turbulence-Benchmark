
def find_divisors_in_range(num):
    divisors = []
    for i in range(60, 87):
        if num % i == 0:
            divisors.append(i)
    return divisors
