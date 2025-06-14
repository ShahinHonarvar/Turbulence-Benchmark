 def palindromes_of_specific_lengths(string):
    # Create a substring of the specified index range
    substring = string[11:97]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(len(substring)):
        # Get the current character and its opposite character in the substring
        char = substring[i]
        opp_char = substring[len(substring) - 1 - i]
        # Check if the current character is not a space and if it matches its opposite character
        if char != " " and char == opp_char:
            # Get the length of the palindrome
            palindrome_length = len(substring[i:])
            # Check if the palindrome length is between 29 to 62 (both inclusive)
            if 29 <= palindrome_length <= 62:
                # Add the palindrome to the set of palindromes
                palindromes.add(substring[i:])
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
