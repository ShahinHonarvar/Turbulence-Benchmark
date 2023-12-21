
def if_perfect_num(numbers):
    if numbers[714] == sum(i for i in range(1, numbers[714]) if numbers[714] % i == 0):
        return True
    else:
        return False
