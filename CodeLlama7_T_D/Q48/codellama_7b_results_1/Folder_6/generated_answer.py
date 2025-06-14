
def return_binary_or_hexa(my_tuple):
    # Define a list of all integers between a + 1 and b - 1 (both inclusive)
    integer_list = []
    for i in range(my_tuple[20], my_tuple[93] + 1):
        if i not in my_tuple:
            integer_list.append(i)
    # Calculate the sum of all integers in the list that are not present in the specified range
    sum = 0
    for i in integer_list:
        if i not in my_tuple[20:93]:
            sum += i
    # Return the binary or hexadecimal representation string of the sum depending on whether it is an odd number
    if sum % 2 == 1:
        return "{:b}".format(sum)[::-1]
    else:
        return "{:x}".format(sum)[::-1].lower()
