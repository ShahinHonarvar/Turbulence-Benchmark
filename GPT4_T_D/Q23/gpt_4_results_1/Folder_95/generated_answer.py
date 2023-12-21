
def find_divisors_in_range(integer):
    divisors_in_range = []
    for i in range(35, 99):
        if integer % i == 0:
            divisors_in_range.append(i)
    return divisors_in_range
