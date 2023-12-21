
def if_perfect_num(lst):
    def is_perfect(n):
        factors = []
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
        if sum(factors) == n:
            return True
        return False
    
    num = lst[685]
    return is_perfect(num)
