
def all_neg_ints_exclusive(numbers):
    neg_nums = []
    for num in numbers[1:8]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums
