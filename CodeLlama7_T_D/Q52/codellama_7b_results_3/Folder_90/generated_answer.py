
def palindrome_of_length_n(string):
    # Split the string into individual characters
    chars = string.split()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each character in the string
    for i in range(len(chars)):
        # Check if the current character is a letter (not a space or punctuation)
        if chars[i].isalpha():
            # Get the lowercase version of the current character
            curr_char = chars[i].lower()

            # Iterate over each character in the string from the current position to the end
            for j in range(i + 1, len(chars)):
                # Check if the current character is a letter (not a space or punctuation)
                if chars[j].isalpha():
                    # Get the lowercase version of the current character
                    other_char = chars[j].lower()

                    # Check if the current character and the other character are the same, but in different cases (e.g. "a" and "A")
                    if curr_char == other_char:
                        # Get the substring of the string from the current position to the end
                        substr = ''.join(chars[i:j + 1])

                        # Check if the substring is a palindrome (i.e. it reads the same forward and backward)
                        if substr == substr[::-1]:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(substr)

    # Return the set of palindromes
    return palindromes
