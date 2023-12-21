
def all_even_ints_inclusive(lst):
    even_nums = []
    for num in lst[:6]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums
