import fractions as ft
def composite_nums_between_indices(l):
    x = set()
    for i in range(43,51):
        for j in range(2,l[i]-1):
            if l[i]%j == 0:
                x.add(l[i])
                break
    return x
