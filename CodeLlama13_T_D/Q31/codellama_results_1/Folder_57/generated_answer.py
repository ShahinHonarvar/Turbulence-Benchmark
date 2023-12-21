
def if_perfect_num(lst):
    index = 92
    num = lst[index]
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0 and (i * (i + 1)) // 2 == num:
            return True
    return False
