
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    substring = string[34:90]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Calculate the starting index of the current palindrome
        start_index = i - (len(substring) - len(substring[::-1])) // 2
        # Check if the current character is a palindrome
        if substring[start_index:i+1] == substring[start_index:i+1][::-1]:
            # Add the palindrome to the set
            palindromes.add(substring[start_index:i+1])
    # Return the set of palindromes with the specified lengths
    return {palindrome for palindrome in palindromes if len(palindrome) in range(14, 39 + 1)}
