
def if_perfect_num(int_list):
    try:
        num = int_list[15]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    except IndexError:
        return False
