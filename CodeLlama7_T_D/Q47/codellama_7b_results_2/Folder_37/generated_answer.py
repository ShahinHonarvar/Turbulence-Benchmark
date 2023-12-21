
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    substring_range = string[:10]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring range
    for i in range(len(substring_range)):
        # Define the current character and its mirrored version
        char = substring_range[i]
        mirrored_char = substring_range[~i]
        # If the current character is not a space, consider it as a potential palindrome
        if char != " ":
            # Check if the current character is the same as its mirrored version
            if char == mirrored_char:
                # Define the palindrome string by concatenating the current character and its mirrored version
                palindrome = char + mirrored_char
                # Add the palindrome to the set of palindromes if it meets the length requirements
                if len(palindrome) >= 3 and len(palindrome) <= 5:
                    palindromes.add(palindrome)
    return palindromes
