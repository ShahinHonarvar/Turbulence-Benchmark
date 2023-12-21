
def if_perfect_num(numbers):
    if numbers[94] == sum(set(numbers[:numbers[94]]) - set([numbers[94]])):
        return True
    else:
        return False
