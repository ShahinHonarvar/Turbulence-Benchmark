
def if_perfect_num(lst):
    try:
        num = lst[37]
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num
    except:
        return False
