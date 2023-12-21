
def find_divisors_in_range(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0 and 35 <= i <= 37:
            divisors.append(i)
    return divisors
