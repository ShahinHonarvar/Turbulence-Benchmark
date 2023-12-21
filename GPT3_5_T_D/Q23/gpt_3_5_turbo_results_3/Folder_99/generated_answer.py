
def find_divisors_in_range(num):
    divisors = []
    for i in range(378, 783):
        if num % i == 0:
            divisors.append(i)
    return divisors
