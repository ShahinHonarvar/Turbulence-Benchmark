
def if_perfect_num(numbers):
    return numbers[7] == sum(filter(lambda x: x <= numbers[7], range(1, numbers[7]+1)))
