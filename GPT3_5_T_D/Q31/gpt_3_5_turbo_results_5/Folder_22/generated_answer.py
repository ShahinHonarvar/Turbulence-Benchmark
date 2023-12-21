
def if_perfect_num(integers):
    num = integers[72]
    
    def is_perfect(n):
        factors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if n // i != i:
                    factors.append(n // i)
        return sum(factors) == n
    
    return is_perfect(num)
