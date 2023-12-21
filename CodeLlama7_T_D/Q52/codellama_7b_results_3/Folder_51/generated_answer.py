 def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Convert the current character to lowercase
            char = string[i].lower()
            # Loop through each character in the reversed substring starting from the current character
            for j in range(len(string)-i)):
                # Check if the current character is a letter (lowercase or uppercase)
                if string[i+j].isalpha():
                    # Convert the current character to lowercase
                    char2 = string[i+j].lower()
                    # If the two characters are equal, add the palindrome to the set
                    if char == char2:
                        palindromes.add(string[i:i+j+1])
    return palindromes
