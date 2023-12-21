
def if_perfect_num(numbers):
    index_40 = numbers[40]
    factors = [i for i in range(1, index_40) if index_40 % i == 0]
    return sum(factors) == index_40
