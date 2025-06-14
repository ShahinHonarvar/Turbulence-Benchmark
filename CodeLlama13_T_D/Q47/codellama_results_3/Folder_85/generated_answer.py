
def palindromes_of_specific_lengths(string):
    # find all palindromes in the string
    palindromes = []
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                palindromes.append(string[i:j+1])
    
    # filter palindromes by length and case-insensitivity
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 6 and len(palindrome) <= 9 and all(c.isalpha() for c in palindrome):
            filtered_palindromes.append(palindrome)
    
    # return the set of filtered palindromes
    return set(filtered_palindromes)
