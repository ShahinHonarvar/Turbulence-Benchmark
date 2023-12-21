
def palindromes_of_specific_lengths(string):
    # Find the palindromes in a case-insensitive manner
    string = string.lower()
    # Only consider palindromes occurring in the substring from index 0 to index 4, both inclusive
    substring = string[:5]
    # Only consider palindromes of lengths between 3 to 4 (both inclusive)
    palindromes = []
    for i in range(3, 5):
        # Find all the palindromes of length i in the substring
        palindromes += [substring[j:j+i] for j in range(len(substring)-i+1) if substring[j:j+i] == substring[j:j+i][::-1]]
    return set(palindromes)
