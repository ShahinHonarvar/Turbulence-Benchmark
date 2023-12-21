
def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(3, x+1):
        is_prime = True
        for j in range(2, len(str(i))+1):
            if str(i)[j-1] == '0':
                is_prime = False
                break
        if is_prime:
            lst.append(i)
    return sorted(lst, reverse=True)
