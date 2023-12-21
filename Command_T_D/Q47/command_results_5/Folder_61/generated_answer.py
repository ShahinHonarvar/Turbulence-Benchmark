def palindromes_of_specific_lengths(text):
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate through each character in the text
    for index, character in enumerate(text):
        # If the character is a letter, add it to the palindrome
        if character.isalpha():
            length = index + 1
            while length < 31 and length >= 20:
                # If the next character is a letter, add it to the palindrome
                if text[length].isalpha():
                    length += 1
                else:
                    # If the next character is not a letter, stop adding characters to the palindrome
                    break
            # Add the palindrome to the set
            palindromes.add(character.lower() + text[length:length + length])
    return palindromes
