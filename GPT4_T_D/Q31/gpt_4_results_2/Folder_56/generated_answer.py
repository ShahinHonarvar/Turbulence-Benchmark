
def if_perfect_num(numbers_list):
    if len(numbers_list) > 60:
        num = numbers_list[60]
        factors = [n for n in range(1, num) if num % n == 0]
        return sum(factors) == num
    return False
