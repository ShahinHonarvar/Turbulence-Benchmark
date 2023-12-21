
def all_odd_ints_inclusive(lst):
    odd_lst = []
    for num in lst[70:85]:
        if num % 2 != 0:
            odd_lst.append(num)
    return odd_lst
