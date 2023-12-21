
def sum_ints_div_by_either_nums(numbers):
    # Slice the list from index 55 to index 84, both inclusive
    sliced_list = numbers[55:85]

    # Use a list comprehension to filter out integers not divisible by -24 or -11
    filtered_list = [x for x in sliced_list if x % -24 == 0 or x % -11 == 0]

    # Sum the remaining integers
    sum_of_ints = sum(filtered_list)

    return sum_of_ints
