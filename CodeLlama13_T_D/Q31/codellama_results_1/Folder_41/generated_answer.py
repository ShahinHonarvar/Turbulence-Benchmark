
def if_perfect_num(lst):
    if len(lst) < 85: return False
    i = lst[84]
    s = sum(range(1, int(i**0.5)+1))
    return s*2 == i and not any(s in {j: True} for j in range(int(i**0.5), i+1) if (j-i)/i < 1e-6)
