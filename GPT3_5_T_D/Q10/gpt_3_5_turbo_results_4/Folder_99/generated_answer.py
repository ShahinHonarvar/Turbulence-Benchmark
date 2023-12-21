
def all_odd_ints_exclusive(lst):
    odd_ints = []
    for num in lst[295:573]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints
