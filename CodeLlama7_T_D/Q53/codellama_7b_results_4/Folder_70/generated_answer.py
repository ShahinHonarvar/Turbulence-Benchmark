 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Get the lowercase version of the current character
            lowercase_char = string[i].lower()
            # Loop through each character in the remaining part of the string
            for j in range(i + 1, len(string)):
                # Check if the current character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Get the lowercase version of the current character
                    lowercase_char2 = string[j].lower()
                    # Check if the two characters are the same in lowercase
                    if lowercase_char == lowercase_char2:
                        # If they are, then we have found a palindrome of length at least n
                        palindromes.add(string[i : j + 1])
    return palindromes
