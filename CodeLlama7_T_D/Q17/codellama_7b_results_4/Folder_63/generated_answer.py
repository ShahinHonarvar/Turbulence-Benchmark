
def all_ints_div_by_both_two_nums(my_list):
    # Find the first index where a number is not divisible by both 81 and 64
    first_non_divisible_index = next((i for i, x in enumerate(my_list) if x % 81 != 0 or x % 64 != 0), len(my_list))
    # If no such indices exist, return an empty list
    if first_non_divisible_index == len(my_list):
        return []

    # Find the last index where a number is not divisible by both 81 and 64

    last_non_divisible_index = next((i for i, x in enumerate(my_list) if x % 81 != 0 or x % 64 != 0), len(my_list))

    # Return the list of all integers divisible by both 81 and 64 from index 31 to index 50, both inclusive

    return my_list[31:first_non_divisible_index] + my_list[last_non_divisible_index:]
