
def if_perfect_num(my_list):
    if len(my_list) <= 59:
        return False
    n = my_list[59]
    if n == sum([i for i in range(1, int(n**0.5) + 1) if n % i == 0]):
        return True
    else:
        return False
