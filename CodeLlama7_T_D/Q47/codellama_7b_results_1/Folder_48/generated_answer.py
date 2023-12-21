
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start_index = 155
    end_index = 283
    substring = string[start_index:end_index]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Check if the character is a letter (not punctuation or whitespace)
        if substring[i].isalpha():
            # Create a copy of the substring starting from the current index
            substr = substring[i:]
            # Reverse the copy of the substring
            rev_substr = substr[::-1]
            # Check if the reversed substring is equal to the original substring
            if substr == rev_substr:
                # Add the palindrome to the set of palindromes
                palindromes.add(substr)
    # Return the set of palindromes that meet the requirements
    return palindromes
