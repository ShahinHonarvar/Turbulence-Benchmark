
def palindromes_of_specific_lengths(string):
    substring = string[32:80].lower()
    palindromes = set()

    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]
            if word.isalpha() and word == word[::-1]:
                palindromes.add(word)

    return palindromes
