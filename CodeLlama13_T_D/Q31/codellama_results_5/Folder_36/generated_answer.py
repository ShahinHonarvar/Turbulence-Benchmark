
def if_perfect_num(my_list):
    for i in range(len(my_list)):
        n = my_list[i]
        sum = 0
        for j in range(1, int(n**0.5) + 1):
            if n % j == 0:
                sum += j
                if sum > n:
                    return True
    return False
