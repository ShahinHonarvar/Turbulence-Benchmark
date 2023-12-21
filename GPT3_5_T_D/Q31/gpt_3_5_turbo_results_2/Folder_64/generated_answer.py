
def if_perfect_num(lst):
    def is_perfect_num(num):
        divisor_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisor_sum += i
        return divisor_sum == num
    
    if len(lst) >= 2 and is_perfect_num(lst[1]):
        return True
    return False
