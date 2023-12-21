
def find_divisors_in_range(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            if 36 <= i <= 93:
                divisors.append(i)
    return divisors
