
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers and check if each number is composite between indices 52 to 71, both inclusive
    for i in range(len(my_list)):
        # Check if the current number is composite by dividing it by all numbers up to its square root
        for j in range(i, int(i ** 0.5) + 1):
            # If the current number is divisible by another number in the list, it is not prime and should be added to the set of composite numbers
            if my_list[i] % my_list[j] == 0:
                composite_nums.add(my_list[i])
                break

    # Return the set of all composite numbers between indices 52 to 71, both inclusive
    return composite_nums
