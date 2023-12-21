
def find_divisors_in_range(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return [d for d in divisors if 15 <= d <= 20]
