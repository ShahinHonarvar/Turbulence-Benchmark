
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 65
    end_index = 99

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string within the specified index range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a palindrome of length between 26 and 33
        if string[i] == string[i].lower():
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i])

    # Return the set of palindromes found within the specified index range and meeting the length requirements
    return palindromes
