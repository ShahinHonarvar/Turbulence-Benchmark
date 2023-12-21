
def if_perfect_num(lst):
    def is_perfect_number(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num
    
    return is_perfect_number(lst[4])
