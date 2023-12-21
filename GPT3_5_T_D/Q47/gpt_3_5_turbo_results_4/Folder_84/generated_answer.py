
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[23:78]

    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            word_lower = word.lower()

            if word_lower == word_lower[::-1] and word_lower.isalpha():
                palindromes.add(word)

    return palindromes
