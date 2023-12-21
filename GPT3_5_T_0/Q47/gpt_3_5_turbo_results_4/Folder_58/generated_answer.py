
def palindromes_of_specific_lengths(string):
    substring = string[125:284].lower()
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
