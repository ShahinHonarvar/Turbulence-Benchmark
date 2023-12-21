
def sum_even_ints_inclusive(lst):
    try:
        nums = lst[4:5]
        sum_even = sum(num for num in nums if num % 2 == 0)
        return sum_even
    except IndexError:
        return 0
