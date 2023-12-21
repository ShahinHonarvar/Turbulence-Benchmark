
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the current character is a letter
        if s[i].isalpha():
            # Loop through each character in the string from the current position to the end
            for j in range(i + 1, len(s) + 1):
                # Check if the substring starting at the current position and ending at the index 'j' is a palindrome
                if s[i:j].lower() == s[i:j][::-1].lower():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(s[i:j])
    # Return the set of palindromes
    return palindromes
