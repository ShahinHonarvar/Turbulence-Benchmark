
def find_divisors_in_range(integer):
    divisors = []
    for i in range(16, 54):
        if integer % i == 0:
            divisors.append(i)
    return divisors
