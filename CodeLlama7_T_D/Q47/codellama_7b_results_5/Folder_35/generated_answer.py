
def palindromes_of_specific_lengths(string, start_index=34, end_index=90):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through the characters in the specified range
    for i in range(start_index, end_index+1):
        # Check if the character at index i is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ''

            # Loop through the characters in the specified range in reverse order
            for j in range(start_index, end_index+1):
                # Check if the character at index j is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Add the character at index j to the palindrome string
                    palindrome += string[j]

            # Check if the palindrome has the required length
            if len(palindrome) >= 14 and len(palindrome) <= 39:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)

    return palindromes
