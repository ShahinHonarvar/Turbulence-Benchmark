
def palindromes_of_specific_lengths(string):
    substr = string[18:99]
    palindromes = set()
    for i in range(31, 52):
        for j in range(len(substr) - i + 1):
            word = substr[j:j+i]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
