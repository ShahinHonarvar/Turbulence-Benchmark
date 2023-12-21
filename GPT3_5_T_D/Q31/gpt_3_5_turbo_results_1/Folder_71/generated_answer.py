
def if_perfect_num(numbers):
    if numbers[78] == calculate_sum_of_divisors(numbers[78]):
        return True
    else:
        return False

def calculate_sum_of_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)
