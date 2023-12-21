
def palindromes_of_specific_lengths(string):
    substring = string[11:97].lower()
    palindromes = set()
    for length in range(45, 53):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
