
def sum_even_ints_inclusive(lst):
    even_nums = [num for num in lst if num % 2 == 0]
    return sum(even_nums[:9]) if len(even_nums) >= 9 else 0
