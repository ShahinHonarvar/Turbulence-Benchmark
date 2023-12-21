
def all_odd_ints_exclusive(lst):
    subrange = lst[370:983]
    odd_numbers = [num for num in subrange if num % 2 != 0]
    return odd_numbers
