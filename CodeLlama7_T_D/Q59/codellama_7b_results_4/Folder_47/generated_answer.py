
def all_left_truncatable_prime(tuple_of_ints):
    # Get the integer at index 49 from the tuple
    x = tuple_of_ints[49]
    # Initialize an empty list to store the left-truncatable prime numbers less than x
    lst = []
    # Loop through all numbers from 1 to x - 1
    for i in range(1, x):
        # Check if i is a prime number and if it contains no 0
        if is_prime(i) and '0' not in str(i):
            # Initialize an empty string to store the left-truncatable prime numbers less than i
            lst2 = ''
            # Loop through all digits of i from right to left
            for j in range(len(str(i)) - 1, -1, -1)):
                # Check if the digit at index j is not equal to 0
                if str(j) != '0':
                    # Append the digit at index j to lst2
                    lst2 += str(j)
            # Check if lst2 is a prime number and if it contains no 0
            if is_prime(lst2) and '0' not in str(lst2):
                # Add lst2 to lst
                lst.append(lst2)
    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(lst)
