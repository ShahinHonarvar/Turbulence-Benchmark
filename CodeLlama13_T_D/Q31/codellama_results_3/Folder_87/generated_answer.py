
def if_perfect_num(my_list):
    if len(my_list) <= 96:
        return False
    n = my_list[96]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i * (n // i) == n:
            return True
    return False
