
def palindromes_between_indices(s):
    # Create a set to store all palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 10):
        # Check if the current character is a letter
        if s[i].isalpha():
            # Create a copy of the string with all lowercase letters
            lowercase = s.lower()
            # Check if the current character is uppercase or not
            if s[i].isupper():
                # Convert the current character to lowercase
                lowercase = lowercase[:i] + lowercase[i].lower() + lowercase[i+1:]
            # Get the starting and ending indices of the current palindrome
            start = i - 4
            end = i + 5
            # Check if the current palindrome is valid
            if start >= 0 and end < len(s):
                # Add the current palindrome to the set of palindromes
                palindromes.add(lowercase[start:end])
    # Return the set of palindromes
    return palindromes
