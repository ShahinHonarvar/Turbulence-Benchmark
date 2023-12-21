
def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[11:94].lower()

    for length in range(34, 55):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word.isalpha() and word == word[::-1]:
                palindromes.add(word)

    return palindromes
