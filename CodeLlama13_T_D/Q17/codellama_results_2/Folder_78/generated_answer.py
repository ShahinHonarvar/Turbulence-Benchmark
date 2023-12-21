
def all_ints_div_by_both_two_nums(lst):
    lst = lst[34:70]  # Slicing the list from index 34 to index 69, both inclusive
    return [x for x in lst if x % 19 == 0 and x % 32 == 0]  # Using a list comprehension to filter out elements that are divisible by both 19 and 32
