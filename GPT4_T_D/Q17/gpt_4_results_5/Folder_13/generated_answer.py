
def all_ints_div_by_both_two_nums(lst):
    divisible_numbers = []
    for num in lst[13:19]:
        if num % 45 == 0 and num % 20 == 0:
            divisible_numbers.append(num)
    return divisible_numbers
