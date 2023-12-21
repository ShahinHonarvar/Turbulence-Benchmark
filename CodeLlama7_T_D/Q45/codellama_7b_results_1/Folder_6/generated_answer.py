
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each possible length of palindrome between indices 0 and 7
    for length in range(4, len(string) + 1):
        # Get the substring of the given string that occurs between indices 0 and (length - 1)
        sub_string = string[0:length - 1]
        # Iterate through each possible palindrome of the specified length
        for i in range(0, length // 2 + 1):
            # Get the substring of the given string that occurs between indices (i and length - 1)
            sub_palindrome = sub_string[i:length - 1]
            # Check if the palindrome is at least 4 characters long and if it is a palindrome in a case-insensitive manner
            if len(sub_palindrome) >= 4 and sub_palindrome.lower() == sub_palindrome[::-1].lower():
                # Add the palindrome to the set of palindromes
                palindromes.add(sub_palindrome)
    # Return the set of palindromes
    return palindromes
