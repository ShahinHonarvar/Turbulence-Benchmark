
def if_perfect_num(lst):
    def is_perfect_num(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    
    if len(lst) > 92 and is_perfect_num(lst[92]):
        return True
    else:
        return False
