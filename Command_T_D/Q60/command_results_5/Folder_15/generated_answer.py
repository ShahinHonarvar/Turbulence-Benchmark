
import re

def all_left_right_truncatable_prime(tup):
    lst = []
    for num in range(max(tup), 2, -1):
        lst += [str(num)]
        lst += [str(num)]
        if len(lst) > 2:
            lst.sort()
            for lst_idx in range(2, len(lst)):
                if lst[lst_idx - 1] == lst[lst_idx]:
                    break
                elif lst[lst_idx - 1] != lst[lst_idx]:
                    if all(int(i) for i in lst[1:lst_idx]):
                        if re.match("1?0", lst[lst_idx - 1]):
                            lst.remove(lst[lst_idx - 1])
                            break
                    elif all(int(i) for i in lst[lst_idx + 1:]):
                        if re.match("1?0$", lst[lst_idx]):
                            lst.remove(lst[lst_idx])
                            break
        if len(lst) == 2:
            break
    return lst
