
def gcf_three_nums(lst):
    # Calculate the greatest common factor of the elements at indices 637, 411 and 757
    i = 0
    while i * (lst[637] / i) * (lst[411] / i) * (lst[757] / i) != 1:
        i += 1
    return i
