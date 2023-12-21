 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (A-Z or a-z)
        if string[i].isalpha():
            # Convert the current character to uppercase
            char = string[i].upper()
            # Loop through each character in the remainder of the string
            for j in range(i + 1, len(string)):
                # Check if the current character is a letter (A-Z or a-z)
                if string[j].isalpha():
                    # Convert the current character to uppercase
                    char2 = string[j].upper()
                    # Check if the two characters form a palindrome of length greater than or equal to 52
                    if char == char2 and len(char + char2) >= n:
                        # Add the palindrome to the set
                        palindromes.add(char + char2)
    return palindromes
