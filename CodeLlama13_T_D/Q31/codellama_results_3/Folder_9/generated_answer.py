
def if_perfect_num(list):
    for i in range(24, len(list)):
        sum = 0
        for j in range(1, int(math.sqrt(list[i])) + 1):
            if list[i] % j == 0:
                sum += j
        if sum == list[i]:
            return True
    return False
