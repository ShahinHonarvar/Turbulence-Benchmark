
def palindromes_of_specific_lengths(string):
    substring = string[15:94]
    lengths = range(18, 73 + 1)
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()

    for length in lengths:
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1] and all(letter in english_letters for letter in substr.lower()):
                palindromes.add(substr)

    return palindromes
