
def if_perfect_num(lst):
    return lst[851] in [n for n in range(1, int(n**0.5) + 1) if n % i == 0 for i in range(1, int(n**0.5) + 1)]
