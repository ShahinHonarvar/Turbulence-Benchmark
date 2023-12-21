import sys
def all_right_truncatable_prime(n):
    if n[85] < 2:
        return []
    lst = []
    for i in range(2, n[85]):
        if str(i) in n[85]:
            continue
        x = int(str(i) + n[85][:len(str(i))])
        if x == i or x == 0:
            continue
        if all(str(x) % i for i in range(2, x)):
            lst.append(x)
    return sorted(lst)
