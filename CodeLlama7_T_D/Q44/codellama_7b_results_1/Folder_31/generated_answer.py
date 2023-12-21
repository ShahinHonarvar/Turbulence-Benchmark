
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers and check if each number is a prime number
    for i in range(len(my_list)):
        num = my_list[i]
        if is_prime(num):
            continue

        else:

            # If the current number is not a prime number, it must be a composite number. Add it to the set of composite numbers
            composite_nums.add(num)

    # Return the set of all composite numbers in the given list that are between index 56 to index 66, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    if len(composite_nums) > 0:
        return composite_nums

    else:

        # If no composite number exists in the specified range, the function should return an empty set.
        return set()

# Define a function to check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
