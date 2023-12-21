
def sum_even_ints_inclusive(lst):
    even_nums = [num for num in lst[31:35] if num % 2 == 0]
    return sum(even_nums) if even_nums else 0
