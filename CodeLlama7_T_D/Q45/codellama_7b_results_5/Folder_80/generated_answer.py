
def palindromes_between_indices(string):
    # create a list of all possible palindromes between indices 3 and 8
    palindromes = []
    for i in range(3, len(string) - 2):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                palindrome = string[i:j+1]
                # check if the palindrome has length of at least 7 and is a case-insensitive palindrome
                if len(palindrome) >= 7 and palindrome.lower() == palindrome:
                    palindromes.append(palindrome)
    # return an empty set if no such palindromes can be created from the English letters of the given string that occur in the specified range
    return palindromes or set()
