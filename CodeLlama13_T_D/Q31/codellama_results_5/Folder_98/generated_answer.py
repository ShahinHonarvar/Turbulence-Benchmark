
def if_perfect_num(numbers):
    if len(numbers) < 5:
        return False
    elif numbers[4] == sum(divisors(numbers[4])):
        return True
    else:
        return False
