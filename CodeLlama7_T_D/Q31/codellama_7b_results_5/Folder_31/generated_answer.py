
def if_perfect_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Check if the integer at index 66 is a perfect number
    for i in range(len(my_list)):
        if my_list[i] == 66 and perfect_number(my_list[i]):
            return True

    # If no perfect number was found, return False
    return False

# Check if a number is a perfect number
def perfect_number(n):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i

    # If the sum of the integer's factors is equal to the integer itself, it is a perfect number
    return sum == n
