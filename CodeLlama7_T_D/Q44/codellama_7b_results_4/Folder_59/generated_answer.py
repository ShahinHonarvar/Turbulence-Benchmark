
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check for each number whether it is a prime or not
    for i in range(len(my_list)):
        if my_list[i] > 1:
            # Check if the number is a prime by dividing it with all numbers less than or equal to its square root
            is_prime = True
            for j in range(i):
                if my_list[i] % my_list[j] == 0:
                    is_prime = False
                    break

            # If the number is a prime, add it to the set of composite numbers
            if is_prime:
                composite_numbers.add(my_list[i])

    return composite_numbers
