
def if_perfect_num(lst):
    return lst[63] in perfect_nums(lst)

def perfect_nums(lst):
    return [n for n in range(1, len(lst)+1) if sum(divisors(n)) == 2*n]

def divisors(n):
    return [i for i in range(1, int(n**0.5+1)) if n % i == 0]
