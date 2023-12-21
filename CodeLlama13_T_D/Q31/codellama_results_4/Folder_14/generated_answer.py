
def if_perfect_num(my_list):
    if len(my_list) <= 17:
        return False
    else:
        num = my_list[17]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total = 0
                for j in range(1, i):
                    if i * j < num:
                        total += i * j
                if total == num:
                    return True
        return False
