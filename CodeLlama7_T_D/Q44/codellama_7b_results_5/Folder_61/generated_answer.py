
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if i >= 0 and i <= 7:
            # Check if the current number is not equal to 1, as 1 is considered a prime number
            if num != 1:
                for j in range(2, int(num ** 0.5) + 1):
                    # If the current number is divisible by any number between 2 and its square root plus 1, it is not prime
                    if num % j == 0:
                        break
                else:
                    # If the loop completes without finding a factor, the current number is prime
                    composite_nums.add(num)

    return composite_nums
