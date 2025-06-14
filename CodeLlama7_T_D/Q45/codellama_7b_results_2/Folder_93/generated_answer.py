
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the current character is a letter
        if s[i].isalpha():
            # Get the index of the last occurrence of the current character
            j = len(s) - 1
            while j >= i:
                # Check if the substring starting at index i and ending at index j is a palindrome
                if s[i:j+1] == s[i:j+1][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(s[i:j+1])
                # Decrement j by 1
                j -= 1
    # Return the set of palindromes
    return palindromes
