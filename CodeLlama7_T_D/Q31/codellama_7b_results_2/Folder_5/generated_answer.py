
def if_perfect_num(my_list):
    # Check if the list has at least 68 elements
    if len(my_list) < 68:
        return False

    # Check if the 67th element is a perfect number
    elif my_list[67] == 0:
        return True

    else:

        # Initialize a variable to store the sum of the factors of the 67th element
        sum = 0

        # Loop through all the numbers from 1 to the square root of the 67th element
        for i in range(1, int(my_list[67]) ** 0.5) + 1:
            # Check if the number is a factor of the 67th element
            if my_list[67] % i == 0:
                # Add the factor to the sum
                sum += i

        # Check if the sum of the factors is equal to the 67th element
        if sum == my_list[67]:
            return True

        else:

            return False
