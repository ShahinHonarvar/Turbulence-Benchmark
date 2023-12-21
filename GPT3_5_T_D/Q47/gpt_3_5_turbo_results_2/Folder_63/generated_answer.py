
def palindromes_of_specific_lengths(string):
    substring = string[33:86]
    string = string.lower()
    palindromes = set()

    for length in range(26, 32):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)

    return palindromes
