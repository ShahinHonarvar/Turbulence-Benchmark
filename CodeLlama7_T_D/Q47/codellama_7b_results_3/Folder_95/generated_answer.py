
def palindromes_of_specific_lengths(string):
    # Define the substring range for palindromes
    substring = string[12:56]
    # Initialize an empty set to store palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Define the starting index for the current palindrome
        start_index = i

        # Define the ending index for the current palindrome
        end_index = len(substring) - i

        # Check if the substring from the starting index to the ending index is a palindrome
        if substring[start_index:end_index] == substring[start_index:end_index][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substring[start_index:end_index])

    # Return the set of palindromes that meet the requirements
    return palindromes
