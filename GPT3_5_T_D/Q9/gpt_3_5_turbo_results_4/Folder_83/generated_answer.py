
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for num in lst[90:201]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints
