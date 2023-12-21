
def if_perfect_num(lst):
    return lst[733] in perfect_numbers(lst)

def perfect_numbers(lst):
    return [n for n in lst if sum(divisors(n)) == 2*n]

def divisors(n):
    return [d for d in range(1, int(sqrt(n)+1)) if n % d == 0]
