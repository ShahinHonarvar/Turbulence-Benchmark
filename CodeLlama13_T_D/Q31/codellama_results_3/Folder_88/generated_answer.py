
def if_perfect_num(my_list):
    if my_list[46] > 0:
        for i in range(1, my_list[46] + 1):
            if my_list[46] % i == 0 and sum(divisors(i)) == my_list[46]:
                return True
    return False
