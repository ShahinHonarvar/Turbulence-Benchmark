
def palindromes_of_specific_lengths(string):
    substring = string[12:93]
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes
