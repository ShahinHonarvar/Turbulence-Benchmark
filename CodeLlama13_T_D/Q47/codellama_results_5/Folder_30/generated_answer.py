
def palindromes_of_specific_lengths(string):
    substr = string[14:90]
    palindromes = set()
    for i in range(55, 72):
        for j in range(len(substr) - i + 1):
            word = substr[j:j+i].lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
