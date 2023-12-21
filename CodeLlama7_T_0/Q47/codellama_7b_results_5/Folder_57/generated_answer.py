
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    substring = string[16:94]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Define the starting and ending indices of the current character
        start_index = i
        end_index = len(substring) - 1 - i
        # Check if the current character is a palindrome
        if substring[start_index] == substring[end_index]:
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over each character in the substring starting from the current character
            for j in range(start_index, end_index + 1):
                # Add the current character to the palindrome string
                palindrome += substring[j]
            # Check if the palindrome has a length between 39 and 52 (both inclusive)
            if len(palindrome) >= 39 and len(palindrome) <= 52:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
