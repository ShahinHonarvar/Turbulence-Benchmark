
def sum_even_ints_inclusive(lst):
    even_sum = sum([num for num in lst[59:98] if num%2 == 0])
    return even_sum if even_sum else 0
