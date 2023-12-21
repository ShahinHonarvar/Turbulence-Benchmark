 def palindromes_between_indices(string):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # get the substring starting from index i and ending at index 5 (inclusive)
        substring = string[i:i+5]
        # check if the substring is a palindrome
        if substring == substring[::-1]:
            # add the palindrome to the set
            palindromes.add(substring)
    return palindromes
