
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for num in num_list[543:585]:
        if num % -553 == 0 and num % -737 == 0:
            result.append(num)
    return result
