
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 926 is a perfect number
    if my_list[926] == 0 or my_list[926] % 10 != 0:
        return False

    # Calculate the sum of the factors of the element at index 926
    sum = 0
    for i in range(1, int(my_list[926]) / 2 + 1):
        if my_list[926] % i == 0:
            sum += i

    # Return true if the element at index 926 is a perfect number and false otherwise
    return sum == my_list[926]
