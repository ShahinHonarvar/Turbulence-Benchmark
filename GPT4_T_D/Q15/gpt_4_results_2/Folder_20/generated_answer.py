
def sum_odd_ints_inclusive(int_list):
    sublist = int_list[56:67]
    odd_ints = [num for num in sublist if num % 2 != 0]
    if not odd_ints:
        return 0
    else:
        return sum(odd_ints)
