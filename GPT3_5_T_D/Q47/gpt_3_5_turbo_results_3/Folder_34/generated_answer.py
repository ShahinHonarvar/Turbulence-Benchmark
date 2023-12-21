
def palindromes_of_specific_lengths(string):
    substring = string[200:301]
    palindromes = set()
    for i in range(len(substring)-9):
        for j in range(10, 51):
            word = substring[i:i+j].lower()
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes
