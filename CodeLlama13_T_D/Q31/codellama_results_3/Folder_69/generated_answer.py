
def if_perfect_num(lst):
    if len(lst) <= 459:
        return False
    n = lst[459]
    return n == sum(range(1, int(n**0.5) + 1)) and all(n % i for i in range(2, int(n**0.5)))
