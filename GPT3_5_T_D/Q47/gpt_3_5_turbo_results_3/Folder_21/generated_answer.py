
def palindromes_of_specific_lengths(string):
    substring = string[100:296].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 136, min(i + 161, len(substring) + 1)):
            sub = substring[i: j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
