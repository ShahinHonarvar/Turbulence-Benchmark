
def if_perfect_num(numbers):
    index_val = numbers[45]
    sum_of_factors = sum(i for i in range(1, index_val) if index_val % i == 0)
    return sum_of_factors == index_val
