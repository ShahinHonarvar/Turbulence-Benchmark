
def sum_of_divisors_in_range(integer):
    divisors = []
    for i in range(1, integer + 1):
        if integer % i == 0 and 403 <= i <= 514:
            divisors.append(i)
    return sum(divisors)
