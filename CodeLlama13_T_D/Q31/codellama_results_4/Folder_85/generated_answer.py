
def if_perfect_num(my_list):
    if len(my_list) <= 23:
        return False
    n = my_list[23]
    sum_of_divisors = sum(i for i in range(1, int(n**0.5)+1) if n % i == 0)
    return sum_of_divisors == n
