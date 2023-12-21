
def if_perfect_num(numbers):
    if numbers[537] == sum([i for i in range(1, numbers[537]) if numbers[537] % i == 0]):
        return True
    else: 
        return False
