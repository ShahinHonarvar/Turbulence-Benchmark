
def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return [d for d in divisors if 46 <= d <= 65]
