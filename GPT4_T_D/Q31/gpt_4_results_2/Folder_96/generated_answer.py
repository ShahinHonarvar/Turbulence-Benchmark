
def if_perfect_num(numbers):
    index_num = numbers[47]
    divisors = [num for num in range(1, index_num) if index_num % num == 0]
    return sum(divisors) == index_num
