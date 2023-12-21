
def if_perfect_num(int_list):
    num = int_list[7]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
