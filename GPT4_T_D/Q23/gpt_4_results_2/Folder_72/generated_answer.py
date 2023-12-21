
def find_divisors_in_range(integer):
    return [i for i in range(32, 91) if integer % i == 0]
