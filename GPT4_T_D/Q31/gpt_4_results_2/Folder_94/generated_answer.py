
def if_perfect_num(numbers):
    perfect_num = numbers[93]
    divisors = [i for i in range(1, perfect_num) if perfect_num % i == 0]
    return sum(divisors) == perfect_num
