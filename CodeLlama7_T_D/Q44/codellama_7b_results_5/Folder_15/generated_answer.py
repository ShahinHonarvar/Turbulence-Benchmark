
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if i >= 0 and i <= 3:
            if is_composite(num):
                composite_nums.add(num)
    # Return the set of all composite numbers between index 0 to index 3, both inclusive
    return composite_nums

def is_composite(n):
    # Check if n is greater than 1
    if n <= 1:
        return False

# Iterate from 2 to the square root of n
for i in range(2, int(math.sqrt(n))) + 1):

    # If n is divisible by i, it is not prime
    if n % i == 0:

        return False
