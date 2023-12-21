 def all_left_truncatable_prime(tuple):
    # Initialize an empty list for storing the left-truncatable prime numbers
    leftTruncatablePrimeNumbers = []
    # Iterate over the tuple elements from index 85 and check if each element is a prime number
    for element in tuple[85:]:
        # Check if the current element is a prime number using the Miller-Rabin primality test
        if miller_rabin(element, 10):
            # Initialize an empty string to store the left-truncatable prime number
            leftTruncatablePrimeNumber = ""
            # Iterate over each digit of the current element
            for digit in str(element):
                # Check if the current digit is not 0 and is a prime number using the Miller-Rabin primality test
                if digit != "0" and miller_rabin(int(digit), 10):
                    # Append the current digit to the leftTruncatablePrimeNumber string
                    leftTruncatablePrimeNumber += str(digit)
            # Check if the leftTruncatablePrimeNumber string is not empty and is a prime number using the Miller-Rabin primality test
            if leftTruncatablePrimeNumber != "" and miller_rabin(int(leftTruncatablePrimeNumber), 10):
                # Append the current element to the list of left-truncatable prime numbers
                leftTruncatablePrimeNumbers.append(element)
    # Sort the list of left-truncatable prime numbers in ascending order
    leftTruncatablePrimeNumbers.sort()
    # Return the sorted list of left-truncatable prime numbers
    return leftTruncatablePrimeNumbers

def miller_rabin(n, k):
    # Initialize a boolean variable to store whether or not n is a prime number
    isPrime = False

    # Check if n is equal to 2 or 1

    if n == 2 or n == 1:
        # Set the boolean variable to True
        isPrime = True

    # Check if k is greater than 0 and if n is not equal to 1

    if k > 0 and n != 1:
        # Initialize a list of integers from 2 to k

        for i in range(2, k + 1):
            # Initialize a boolean variable to store whether or not the current number is a prime number
            isCurrentNumberPrime = False

            # Check if the current number is equal to n

            if i == n:
                # Set the boolean variable to True
                isCurrentNumberPrime = True

            # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

            elif i != 1 and (i % n) == 1:
                # Set the boolean variable to True
                isCurrentNumberPrime = True

            # Check if the boolean variable is set to True

            if isCurrentNumberPrime:
                # Initialize a list of integers from 2 to k

                for j in range(2, k + 1):
                    # Initialize a boolean variable to store whether or not the current number is a prime number
                    isCurrentNumberPrime = False

                    # Check if the current number is equal to n

                    if j == n:
                        # Set the boolean variable to True
                        isCurrentNumberPrime = True

                    # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                    elif j != 1 and (j % n) == 1:
                        # Set the boolean variable to True
                        isCurrentNumberPrime = True

                    # Check if the boolean variable is set to True

                    if isCurrentNumberPrime:
                        # Initialize a list of integers from 2 to k

                        for l in range(2, k + 1):
                            # Initialize a boolean variable to store whether or not the current number is a prime number
                            isCurrentNumberPrime = False

                            # Check if the current number is equal to n

                            if l == n:
                                # Set the boolean variable to True
                                isCurrentNumberPrime = True

                            # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                            elif l != 1 and (l % n) == 1:
                                # Set the boolean variable to True
                                isCurrentNumberPrime = True

                            # Check if the boolean variable is set to True

                            if isCurrentNumberPrime:
                                # Initialize a list of integers from 2 to k

                                for m in range(2, k + 1):
                                    # Initialize a boolean variable to store whether or not the current number is a prime number
                                    isCurrentNumberPrime = False

                                    # Check if the current number is equal to n

                                    if m == n:
                                        # Set the boolean variable to True
                                        isCurrentNumberPrime = True

                                    # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                    elif m != 1 and (m % n) == 1:
                                        # Set the boolean variable to True
                                        isCurrentNumberPrime = True

                                    # Check if the boolean variable is set to True

                                    if isCurrentNumberPrime:
                                        # Initialize a list of integers from 2 to k

                                        for o in range(2, k + 1):
                                            # Initialize a boolean variable to store whether or not the current number is a prime number
                                            isCurrentNumberPrime = False

                                            # Check if the current number is equal to n

                                            if o == n:
                                                # Set the boolean variable to True
                                                isCurrentNumberPrime = True

                                            # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                            elif o != 1 and (o % n) == 1:
                                                # Set the boolean variable to True
                                                isCurrentNumberPrime = True

                                            # Check if the boolean variable is set to True

                                            if isCurrentNumberPrime:
                                                # Initialize a list of integers from 2 to k

                                                for p in range(2, k + 1):
                                                    # Initialize a boolean variable to store whether or not the current number is a prime number
                                                    isCurrentNumberPrime = False

                                                    # Check if the current number is equal to n

                                                    if p == n:
                                                        # Set the boolean variable to True
                                                        isCurrentNumberPrime = True

                                                    # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                                    elif p != 1 and (p % n) == 1:
                                                        # Set the boolean variable to True
                                                        isCurrentNumberPrime = True

                                                    # Check if the boolean variable is set to True

                                                    if isCurrentNumberPrime:
                                                        # Initialize a list of integers from 2 to k

                                                        for q in range(2, k + 1):
                                                            # Initialize a boolean variable to store whether or not the current number is a prime number
                                                            isCurrentNumberPrime = False

                                                            # Check if the current number is equal to n

                                                            if q == n:
                                                                # Set the boolean variable to True
                                                                isCurrentNumberPrime = True

                                                            # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                                            elif q != 1 and (q % n) == 1:
                                                                # Set the boolean variable to True
                                                                isCurrentNumberPrime = True

                                                            # Check if the boolean variable is set to True

                                                            if isCurrentNumberPrime:
                                                                # Initialize a list of integers from 2 to k

                                                                for r in range(2, k + 1):
                                                                    # Initialize a boolean variable to store whether or not the current number is a prime number

                                                                    isCurrentNumberPrime = False

                                                                    # Check if the current number is equal to n

                                                                    if r == n:
                                                                            # Set the boolean variable to True
                                                                            isCurrentNumberPrime = True

                                                                    # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                                                    elif r != 1 and (r % n) == 1:
                                                                            # Set the boolean variable to True
                                                                                            isCurrentNumberPrime = True

                                                                                    # Check if the boolean variable is set to True

                                                                                    if isCurrentNumberPrime:
                                                                                                # Initialize a list of integers from 2 to k

                                                                                                for s in range(2, k + 1):
                                                                                                            # Initialize a boolean variable to store whether or not the current number is a prime number

                                                                                                            isCurrentNumberPrime = False

                                                                                                            # Check if the current number is equal to n

                                                                                                            if s == n:
                                                                                                                                # Set the boolean variable to True
                                                                                                                                isCurrentNumberPrime = True

                                                                                                                            # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                                                                                                            elif s != 1 and (s % n) == 1:
                                                                                                                                    # Set the boolean variable to True
                                                                                                                                    isCurrentNumberPrime = True

                                                                                                                                # Check if the boolean variable is set to True

                                                                                                                                if isCurrentNumberPrime:
                                                                                                                                                    # Initialize a list of integers from 2 to k

                                                                                                                                                    for t in range(2, k + 1):
                                                                                                                                                            # Initialize a boolean variable to store whether or not the current number is a prime number

                                                                                                                                                            isCurrentNumberPrime = False

                                                                                                                                                            # Check if the current number is equal to n

                                                                                                                                                            if t == n:
                                                                                                                                                                                # Set the boolean variable to True
                                                                                                                                                                isCurrentNumberPrime = True

                                                                                                                                                            # Check if the current number is not equal to 1 and if the remainder of dividing the current number by n is equal to 1

                                                                                                                                            elif t != 1 and (t % n) == 1:
                                                                                                                                                                # Set the boolean variable to True
                                                                                                                                                                isCurrentNumberPrime = True

                                                                                                                                                            # Check if the boolean variable is set to True

                                                                                                                                                            if isCurrentNumberPrime:
                                                                                                                                                                                # Print the current number

#                                                                                                                                                                                print(t)

# Write a function that takes in a string and returns True or False if the string is a palindrome or not.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward.

def palindrome_checker(word):
        # Initialize an empty list of characters to store each letter in the word

        letters = []

        # Check if the length of the word is greater than 0

        if len(word) > 0:
                # Loop through each letter in the word

                for letter in word:
                        # Add each letter to the list of characters

                        letters.append(letter)

                        # Check if the length of the list is greater than 1

                        if len(letters) > 1:
                                # Remove the last item from the list of characters

                                letters.pop()

                # Check if the first and last items in the list of characters are equal to each other

                if letters[0] == letters[-1]:
                        # Return True

                        return True

                # Otherwise, return False


                else:
                        return False

        # If the length of the word is 0 or less, return False

        else:
                return False
