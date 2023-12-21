
def if_perfect_num(num_list):
    num = num_list[95]
    sum = 1
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
    if sum == num:
        return True
    else:
        return False
