 def palindromes_of_specific_lengths(string):
    # Find the starting and ending indices of the substring in question
    start = 155
    end = 283

    # Create a list to store all possible palindromes within the specified index range
    palindromes = []

    # Iterate through each possible length of palindrome between 104 and 120 (both inclusive)
    for length in range(104, 121):
        # Find the center index of the palindrome
        center = int((length - 1) / 2) + start

        # Check if there is a palindrome with the specified length at the center index
        if string[center - (length - 1) // 2: center + (length - 1) // 2 + 1] == \
            string[center - (length - 1) // 2: center + (length - 1) // 2 + 1][::-1]:
            # Add the palindrome to the list of palindromes
            palindromes.append(string[center - (length - 1) // 2: center + (length - 1) // 2 + 1])
    # Return the set of all palindromes that meet the specified criteria
    return set(palindromes)
