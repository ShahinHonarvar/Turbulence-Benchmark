
def if_perfect_num(numbers):
    return numbers[746] == sum(i for i in range(1, numbers[746]) if numbers[746] % i == 0)
