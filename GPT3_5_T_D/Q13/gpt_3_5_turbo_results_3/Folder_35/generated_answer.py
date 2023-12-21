
def find_second_largest_num(numbers):
    sub_list = numbers[30:49]  # Extract sublist from index 30 to 48
    sub_list.sort(reverse=True)  # Sort the sublist in descending order
    if len(sub_list) >= 2:
        return sub_list[1]  # Return the second largest element
    else:
        return None
