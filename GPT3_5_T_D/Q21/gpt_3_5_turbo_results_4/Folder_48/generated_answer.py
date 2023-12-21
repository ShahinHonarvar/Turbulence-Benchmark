
def all_ints_div_by_num(integers):
    divisible_integers = []
    for num in integers[574:745]:
        if num % 649 == 0:
            divisible_integers.append(num)
    return divisible_integers
