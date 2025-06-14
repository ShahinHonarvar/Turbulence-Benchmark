
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers from index 661 to index 924 (both inclusive)
    for i in range(661, 925):
        # Check if the number at the current index is divisible by any of its factors other than 1 and itself
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # If it is divisible by another number, it is not prime
                break

        else:

            # If the loop completes without breaking, the current number is prime
            composite_nums.add(i)

    return composite_nums
