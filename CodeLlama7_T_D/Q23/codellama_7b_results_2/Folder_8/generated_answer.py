
def find_divisors_in_range(n):
    # create a list of all divisors between 48 and 62 (both inclusive)
    divisors = []
    for i in range(48, 63):
        if n % i == 0:
            divisors.append(i)
    return divisors
