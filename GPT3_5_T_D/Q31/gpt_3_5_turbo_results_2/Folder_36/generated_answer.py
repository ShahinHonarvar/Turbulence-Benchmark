
def if_perfect_num(numbers):
    return sum(n for n in range(1, numbers[990]) if numbers[990] % n == 0) == numbers[990]
