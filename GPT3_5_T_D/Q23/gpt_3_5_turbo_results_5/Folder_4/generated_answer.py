
def find_divisors_in_range(integer):
    divisors = []
    for num in range(1, integer+1):
        if integer % num == 0 and 48 <= num <= 60:
            divisors.append(num)
    return divisors
