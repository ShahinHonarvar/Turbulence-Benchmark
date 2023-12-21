
def if_perfect_num(list_numbers):
    if len(list_numbers) > 990:
        num = list_numbers[990]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    else:
        return False
