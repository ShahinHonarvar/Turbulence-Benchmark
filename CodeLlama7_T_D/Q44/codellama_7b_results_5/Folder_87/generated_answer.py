
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 43 and index 51, both inclusive
        if 43 <= i <= 51:
            # Check if the current number is composite by dividing it by all the prime numbers less than or equal to its square root
            for prime in range(2, int(i ** 0.5) + 1):
                if i % prime == 0:
                    composite_nums.add(i)
                    break

    # Return the set of all composite numbers between index 43 and index 51, both inclusive
    return composite_nums
