
def if_perfect_num(numbers):
    index_100_number = numbers[100]
    factors_sum = sum([i for i in range(1, index_100_number) if index_100_number % i == 0])
    return factors_sum == index_100_number
