
def palindromes_of_specific_lengths(string):
    # Find the substring containing the specified index range
    substring = string[12:92]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(len(substring)):
        # Get the current character and its opposite character
        char = substring[i]
        opp_char = substring[~i]
        # Check if the current character is a letter and its opposite character is also a letter
        if char.isalpha() and opp_char.isalpha():
            # Check if the current character is the same as its opposite character
            if char == opp_char:
                # Add the current character to the set of palindromes
                palindromes.add(char)
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
