
def if_perfect_num(lst):
    def is_perfect(num):
        if num <= 1:
            return False
        divisors_sum = sum(i for i in range(1, num//2 + 1) if num % i == 0)
        return divisors_sum == num
    
    if len(lst) > 13 and is_perfect(lst[13]):
        return True
    return False
