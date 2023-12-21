
def find_divisors_in_range(integer):
    divisors = []
    for i in range(7, 10):
        if integer % i == 0:
            divisors.append(i)
    return divisors
