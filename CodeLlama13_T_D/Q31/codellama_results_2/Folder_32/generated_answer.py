
def if_perfect_num(my_list):
    n = my_list[849]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
