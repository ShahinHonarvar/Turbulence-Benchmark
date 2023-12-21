
def if_perfect_num(my_list):
    # Check if the list has at least 98 elements
    if len(my_list) < 98:
        return False

    # Calculate the sum of the factors of 10000
    sum = 0
    for i in range(2, int(math.sqrt(10000)) + 1)):
        if 10000 % i == 0:
            sum += i

    # Check if the integer at index 97 is equal to the sum of its factors
    if my_list[97] == sum:
        return True

    else:

        return False
