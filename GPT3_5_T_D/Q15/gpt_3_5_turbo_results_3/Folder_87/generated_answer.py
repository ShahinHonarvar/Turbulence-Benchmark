
def sum_odd_ints_inclusive(lst):
    odd_nums = []
    for num in lst[36:47]:
        if num % 2 != 0:
            odd_nums.append(num)
    return sum(odd_nums) if odd_nums else 0
