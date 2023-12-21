
def if_perfect_num(lst):
    def is_perfect(num):
        if num <= 0:
            return False
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    
    return is_perfect(lst[126])
