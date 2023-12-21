
def find_divisors_in_range(integer):
    divisors = []
    for i in range(1, integer + 1):
        if integer % i == 0 and 42 <= i <= 77:
            divisors.append(i)
    return divisors
