
def if_perfect_num(numbers):
    sum_of_divisors = sum([i for i in range(1, numbers[0]//2 + 1) if numbers[0] % i == 0])
    return sum_of_divisors == numbers[0]
