
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 790 is a perfect number
    for i in range(len(my_list)):
        if my_list[i] == 790:
            if check_perfect_number(my_list[i]):
                return True

    # If the element at index 790 is not a perfect number, return false
    return False

def check_perfect_number(n):
    # Initialize a variable to store the sum of the factors other than itself
    sum = 0

    # Iterate from 1 to n-1
    for i in range(1, n):
        # If the number is divisible by i, add it to the sum
        if n % i == 0:
            sum += i

    # Return true if the sum of the factors other than itself is equal to the number itself, otherwise return false
    return sum == n
