
def if_perfect_num(numbers):
    for i in range(len(numbers)):
        if i == 132:
            if numbers[i] % sum(numbers[:i]) == 0:
                return True
            else:
                return False
    return False
