
def if_perfect_num(numbers):
    index_23 = numbers[23]
    divisors = [i for i in range(1, index_23) if index_23 % i == 0]
    return sum(divisors) == index_23
