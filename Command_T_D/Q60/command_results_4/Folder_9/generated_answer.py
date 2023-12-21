
def all_left_right_truncatable_prime(n):
    lst = []
    for i in range(2, n[0]):
        x = str(i)
        if len(x) > 1:
            j = 0
            while j < len(x) - 1:
                if x[j] == '0':
                    break
                elif x[len(x) - 1 - j] == '0':
                    break
                elif i % 10 == x[j]:
                    break
                elif i % 10 == x[len(x) - 1 - j]:
                    break
                j += 1
            else:
                lst.append(i)
    return lst
