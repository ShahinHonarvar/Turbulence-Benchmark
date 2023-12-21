
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the given string
    for i in range(len(string)):
        # Check if the current character is between indices 4 and 5 (inclusive)
        if 4 <= i <= 5:
            # Create a substring of the given string starting from the current index and ending at the length of the string
            substr = string[i:]
            # Iterate over each character in the substring
            for j in range(len(substr)):
                # Check if the current character is not equal to the last character of the substring
                if substr[j] != substr[-1]:
                    # Add the palindrome created from the current character and the last character of the substring to the set of palindromes
                    palindromes.add(substr[:-1] + substr[j])
    return palindromes
