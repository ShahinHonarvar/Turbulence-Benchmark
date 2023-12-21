
def if_perfect_num(my_list):
    # Check if the list has at least 926 elements
    if len(my_list) < 926:
        return False

    # Get the value of the element at index 926
    perfect_number = my_list[926]

    # Check if the perfect number is equal to the sum of its proper divisors, excluding itself
    if perfect_number == sum(divisors for i in range(1, perfect_number) if perfect_number % i == 0)):
        return True

    else:

        return False
