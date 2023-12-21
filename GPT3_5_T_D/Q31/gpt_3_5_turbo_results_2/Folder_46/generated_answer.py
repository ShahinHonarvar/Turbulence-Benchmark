
def if_perfect_num(lst):
    if len(lst) >= 454:
        num = lst[453]
        summ = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                summ += i
                if i != num // i:
                    summ += num // i
        return summ == num
    else:
        return False
