 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Convert the character to lowercase
            char = string[i].lower()
            # Loop through each character in the remaining part of the string
            for j in range(i + 1, len(string)):
                # Check if the character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Convert the character to lowercase
                    other_char = string[j].lower()
                    # Check if the two characters are the same (i.e., the character is a palindrome of length 1)
                    if char == other_char:
                        # Add the palindrome to the set
                        palindromes.add(char)
                    # Otherwise, check if the two characters are different but have the same length (i.e., the character is a palindrome of length 2 or greater)
                    else:
                        # Check if the first character is the same as the second-to-last character (i.e., the palindrome has an even number of characters)
                        if char == string[j - 1]:
                            # Add the palindrome to the set
                            palindromes.add(char + other_char)
                    # Check if the first character is different from the second-to-last character (i.e., the palindrome has an odd number of characters)
                    else:
                        # Check if the last two characters are the same (i.e., the palindrome has an odd number of characters)
                        if other_char == string[j - 2]:
                            # Add the palindrome to the set
                            palindromes.add(char + other_char)
    # Return the set of palindromes that have a length greater than or equal to n
    return palindromes
