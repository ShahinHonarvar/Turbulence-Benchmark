
def palindromes_of_specific_lengths(string):
    # Define the required length range for palindromes
    min_length = 10
    max_length = 50
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string, starting from index 10
    for i in range(len(string) - min_length + 1):
        # Check if the substring starting at index i has a length that is within the required range
        if (i + min_length - 1 < len(string)) and (min_length <= (i + max_length - 1) - i + 1) and (max_length >= (i + max_length - 1) - i + 1)):
            # Check if the substring starting at index i is a palindrome
            if string[i:i + min_length - 1] == string[i:i + min_length - 1][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:i + min_length - 1])
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
