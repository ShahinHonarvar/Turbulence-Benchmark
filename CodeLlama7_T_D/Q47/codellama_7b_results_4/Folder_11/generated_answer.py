
def palindromes_of_specific_lengths(string, start_index=24, end_index=97):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character is a letter (A-Z or a-z)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring, starting from the current index and moving backwards
            for j in range(i, start_index - 1, -1):
                # Add the current character to the palindrome string
                palindrome += string[j]
            # Check if the palindrome has a length between 10 and 36 (both inclusive)
            if len(palindrome) >= 10 and len(palindrome) <= 36:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    return palindromes
