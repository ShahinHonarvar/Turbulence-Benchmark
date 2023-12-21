
def if_perfect_num(my_list):
    # Check if the integer at index 6 is a perfect number
    if my_list[6] == 0:
        return False

    else:

        # Calculate the sum of the factors of the integer at index 6
        factor_sum = 0

        for i in range(1, my_list[6]):
            if my_list[6] % i == 0:
                factor_sum += i

        # Return true if the sum of the factors is equal to the integer at index 6, otherwise return false
        if factor_sum == my_list[6]:
            return True

        else:

            return False
