
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(18, 87 + 1):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the current character to uppercase
            current_char = string[i].upper()
            # Loop through each character in the substring starting from index 18 to index 87
            for j in range(18, i + 1):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the current character to uppercase
                    previous_char = string[j].upper()
                    # Check if the current character is equal to the previous character and the length of the substring from index 18 to index i is between 38 and 60 (both inclusive)
                    if current_char == previous_char and 38 <= (i - j + 1) <= 60:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[j:i+1])
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
