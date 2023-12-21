
def sum_even_ints_inclusive(lst):
    even_nums = [num for num in lst[310:371] if num % 2 == 0]
    if even_nums:
        return sum(even_nums)
    else:
        return 0
