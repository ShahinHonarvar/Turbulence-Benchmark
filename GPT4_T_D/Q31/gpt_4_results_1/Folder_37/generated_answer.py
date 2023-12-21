
def if_perfect_num(numbers):
    index_val = numbers[28]
    sum_of_factors = sum([i for i in range(1, index_val) if index_val % i == 0])
    if sum_of_factors == index_val:
        return True
    else:
        return False
