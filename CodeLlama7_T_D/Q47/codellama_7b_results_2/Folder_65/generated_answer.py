
def palindromes_of_specific_lengths(string):
    # Define the required substring range
    start_index = 15
    end_index = 95

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the specified substring range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a palindrome of length between 20 and 66
        if string[i] == string[i][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i])

    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
