
def sum_in_range(my_list):
    # initialize variables
    sum = 0
    valid_numbers = []

    # iterate through the list and append valid numbers to a new list
    for number in my_list:
        if -3 <= number <= 6:
            valid_numbers.append(number)

    # calculate the sum of the valid numbers
    for number in valid_numbers:
        sum += number

    # return the sum
    return sum
