
def sum_even_ints_inclusive(lst):
    even_nums = [num for idx, num in enumerate(lst) if idx >= 3 and idx <= 5 and num % 2 == 0]
    return sum(even_nums) if even_nums else 0
