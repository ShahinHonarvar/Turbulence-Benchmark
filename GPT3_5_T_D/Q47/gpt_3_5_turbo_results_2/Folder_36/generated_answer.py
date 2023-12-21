
def palindromes_of_specific_lengths(string):
    substring = string[124:284].lower()
    palindromes = set()
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            sub = substring[start : start + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
