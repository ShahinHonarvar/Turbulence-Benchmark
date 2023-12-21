
def if_perfect_num(lst):
    def is_perfect(num):
        if num < 6:
            return False
        factors = set([1])
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        return sum(factors) == num
    
    return is_perfect(lst[21])
