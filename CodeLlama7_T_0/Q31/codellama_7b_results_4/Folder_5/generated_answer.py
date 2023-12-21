
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 67 elements
    if len(my_list) < 67:
        return False

    # Get the 67th element of the list
    perfect_number = my_list[67]

    # Check if the perfect number is equal to the sum of its proper divisors
    if perfect_number == sum(divisors for i in range(1, int(perfect_number ** 0.5) + 1) if perfect_number % i == 0])):
        return True

    else:

        return False
