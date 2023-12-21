 def palindrome_of_length_at_least_n(string, n):
    # convert the string to lowercase for case-insensitive search
    string = string.lower()
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # check if the current character is a letter
        if string[i].isalpha():
            # loop through each character in the remaining part of the string
            for j in range(i + 1, len(string) + 1):
                # check if the substring starting from the current character and ending at the 'j'th character is a palindrome
                if string[i:j] == string[i:j][::-1]:
                    # add the palindrome to the set of palindromes
                    palindromes.add(string[i:j])
    # return the set of palindromes with a length greater than or equal to 'n'
    return {x for x in palindromes if len(x) >= n}
