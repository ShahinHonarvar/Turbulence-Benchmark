
def if_perfect_num(lst):
    def is_perfect_num(num):
        factors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                factors_sum += i
        return factors_sum == num
    
    return is_perfect_num(lst[746])
