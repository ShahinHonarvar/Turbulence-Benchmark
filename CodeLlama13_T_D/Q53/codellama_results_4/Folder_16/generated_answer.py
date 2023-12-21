
def palindrome_of_length_at_least_n(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the current character is a letter
        if s[i].isalpha():
            # If it is, check if the substring starting at that index is a palindrome
            if s[i:i+119] == s[i:i+119][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(s[i:i+119])
    
    return palindromes
