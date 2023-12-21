
def palindromes_between_indices(string):
    # Split the string into a list of characters
    chars = list(string)
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible arrangement of English letters
    for i in range(1, 8):
        for j in range(i + 6, len(chars)):
            # Check if the current substring is a palindrome
            if chars[i:j] == chars[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(''.join(chars[i:j]))
    
    return palindromes
