
def palindromes_between_indices(string):
    # create a list of all possible palindromes of length 3 or more
    palindromes = []
    for i in range(len(string) - 2):
        # check if the substring starting at index i and ending at index i + 2 is a palindrome
        if string[i:i + 2] == string[i:i + 2][::-1]:
            # add the palindrome to the list
            palindromes.append(string[i:i + 2])
    return set(palindromes)
