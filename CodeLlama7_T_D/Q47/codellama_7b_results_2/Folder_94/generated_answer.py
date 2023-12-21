
def palindromes_of_specific_lengths(string, start_index=40, end_index=94):
    # Convert string to lowercase for case-insensitive matching
    lowercase_string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring starting at the specified index and ending before the last character of the substring
    for i in range(start_index, end_index):
        # Check if the current character is a letter (i.e., not a whitespace or punctuation character)
        if lowercase_string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over the characters in the substring starting at the current index and ending before the last character of the substring
            for j in range(i, end_index):
                # Check if the current character is a letter (i.e., not a whitespace or punctuation character)
                if lowercase_string[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += lowercase_string[j]
            # Check if the palindrome has the desired length (i.e., between 45 and 51 characters)
            if len(palindrome) >= 45 and len(palindrome) <= 51:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
