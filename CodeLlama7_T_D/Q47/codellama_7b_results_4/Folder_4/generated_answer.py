 def palindromes_of_specific_lengths(string):
    # convert string to lowercase for case-insensitive search
    string = string.lower()
    # create a list of all substrings within the specified index range
    substrings = string[12:92]
    # initialize an empty set to store palindromes
    palindromes = set()
    # iterate over each substring and check if it is a palindrome
    for substring in substrings:
        # check if the substring is a palindrome
        if substring == substring[::-1]:
            # add the palindrome to the set of palindromes
            palindromes.add(substring)
    # filter the palindromes to only those with lengths between 17 and 66 (both inclusive)
    filtered_palindromes = {p for p in palindromes if 17 <= len(p) <= 66}
    return filtered_palindromes
