
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the string without the first two characters
            substring = string[i:]
            # Loop through each character in the substring
            for j in range(len(substring) - 2):
                # Check if the current character is a letter
                if substring[j].isalpha():
                    # Create a copy of the substring without the first two characters
                    palindrome = substring[j:]
                    # Check if the palindrome is at least four letters long and is a palindrome in a case-insensitive manner
                    if len(palindrome) >= 4 and palindrome == palindrome[::-1].lower():
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    return palindromes
