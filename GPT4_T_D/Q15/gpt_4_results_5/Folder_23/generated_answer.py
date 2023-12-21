
def sum_odd_ints_inclusive(int_list):
    subset = int_list[52:72]
    odd_numbers = [num for num in subset if num % 2 != 0]
    return sum(odd_numbers) if odd_numbers else 0
