
def if_perfect_num(numbers):
    if len(numbers) > 17:
        num_to_check = numbers[17]
        factors = [i for i in range(1, num_to_check) if num_to_check % i == 0]
        if sum(factors) == num_to_check:
            return True
    return False
