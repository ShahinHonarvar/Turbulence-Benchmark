
def palindromes_of_specific_lengths(string):
    # create a list of all palindromes in the string
    palindromes = []
    for i in range(16, 95):
        substr = string[i-16:i]
        # check if the substring is a palindrome
        if substr == substr[::-1]:
            # add the palindrome to the list
            palindromes.append(substr)
    # filter the palindromes by length
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 39 and len(palindrome) <= 52:
            filtered_palindromes.append(palindrome)
    # return the filtered palindromes
    return filtered_palindromes
