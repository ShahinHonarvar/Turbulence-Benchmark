
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list and find all integers between 5 and 7, both inclusive
    for i in my_list:
        if 5 <= i <= 7:
            total += i

    return total
