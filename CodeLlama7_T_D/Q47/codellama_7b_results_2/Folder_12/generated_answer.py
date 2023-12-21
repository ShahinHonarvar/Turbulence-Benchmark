
def palindromes_of_specific_lengths(string):
    # find the substring of interest
    substring = string[62:89]
    # create a list of all possible palindromes with lengths between 18 and 21
    palindromes = []
    for i in range(18, 22):
        for j in range(i + 1):
            palindrome = substring[j:i + j]
            if len(palindrome) == i + 1 and palindrome == palindrome[::-1]:
                palindromes.append(palindrome)
    return set(palindromes)
