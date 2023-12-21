
def palindromes_of_specific_lengths(string):
    # Extract the substring from index 39 to index 94, both inclusive
    substring = string[39:94]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Check if the character is a letter (lowercase or uppercase)
        if substring[i].isalpha():
            # Convert the character to lowercase
            lowercase_char = substring[i].lower()
            # Iterate over the characters in the reversed substring
            for j in range(len(substring)-1, -1, -1):
                # Check if the character is a letter (lowercase or uppercase)
                if substring[j].isalpha():
                    # Convert the character to lowercase
                    lowercase_char2 = substring[j].lower()
                    # Check if the two characters are the same (ignoring case)
                    if lowercase_char == lowercase_char2:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(substring[i:j+1])
    # Return the set of palindromes
    return palindromes
