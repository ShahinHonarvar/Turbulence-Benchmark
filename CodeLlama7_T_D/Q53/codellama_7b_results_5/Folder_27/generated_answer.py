
def palindrome_of_length_at_least_n(s, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the current character is a letter (not a digit or punctuation)
        if s[i].isalpha():
            # Convert the current character to lowercase
            c = s[i].lower()
            # Loop through each character in the string starting from the current index
            for j in range(i + 1, len(s)):
                # Check if the next character is a letter (not a digit or punctuation)
                if s[j].isalpha():
                    # Convert the next character to lowercase
                    d = s[j].lower()
                    # Check if the current character and the next character are the same
                    if c == d:
                        # Add the palindrome consisting of the current character and the next character to the set of palindromes
                        palindromes.add(c + d)
    return palindromes
