
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each element is a prime number
    for i in range(42, 68 + 1):
        num = my_list[i]
        if is_prime(num):
            composite_nums.add(num)

    # Return the set of composite numbers between indices 42 and 68
    return composite_nums

# Check if a number is prime or not
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
