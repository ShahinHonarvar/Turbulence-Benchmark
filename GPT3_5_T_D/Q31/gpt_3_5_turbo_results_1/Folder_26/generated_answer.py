
def if_perfect_num(list_of_integers):
    num = list_of_integers[222]
    
    def is_perfect(n):
        factors = []
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
        return sum(factors) == n
    
    return is_perfect(num)
