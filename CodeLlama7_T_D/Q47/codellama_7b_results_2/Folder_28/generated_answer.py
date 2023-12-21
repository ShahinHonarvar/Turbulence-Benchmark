
def palindromes_of_specific_lengths(string):
    # Define the substring of interest
    substr = string[32:71]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Get the current character and its opposite
        curr_char = substr[i]
        opp_char = curr_char.lower() if curr_char.isupper() else curr_char.upper()
        # If the current character is not equal to its opposite, continue to the next iteration
        if curr_char != opp_char:
            continue

        # Get the length of the current palindrome
        palindrome_len = len(substr[i:]) - len(substr[:i])

        # If the length of the current palindrome is not within the specified range, continue to the next iteration
        if not (21 <= palindrome_len <= 32):
            continue

        # Add the current palindrome to the set of palindromes
        palindromes.add(substr[i:])

    # Return the set of palindromes found in the substring
    return palindromes
