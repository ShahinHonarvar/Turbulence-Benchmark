 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    right_prime = []
    # Iterate through the tuple of positive integers

    for x in tuple:
        # Check if x is a prime number

        if is_prime(x) == True:
            # Initialize an empty string to store the last rightmost digit of x

            rdigit = ""

            # Iterate through the digits of x from right to left

            for i in range(len(str(x))) - 1, -1, -1:
                # Check if the current digit is equal to the last rightmost digit

                if str(x)[i] == rdigit:
                    # Remove the last rightmost digit of x and check if it is still a prime number

                    temp = int(str(x)[:i] + str(x)[i + 1:]))
                    if is_prime(temp) == True:
                        # Append the removed rightmost digit to the list of right-truncatable prime numbers

                        right_prime.append(temp)

                    break

                # If the current digit is not equal to the last rightmost digit, then it is the last rightmost digit

                else:
                    rdigit = str(x)[i]

            # Sort the list of right-truncatable prime numbers in descending order

            right_prime.sort(reverse=True)

        return right_prime
