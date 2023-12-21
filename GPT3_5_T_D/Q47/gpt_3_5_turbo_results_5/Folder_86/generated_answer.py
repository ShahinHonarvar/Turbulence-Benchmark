
def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    substring = substring.lower()
    palindromes = set()
    for length in range(34, 56):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
