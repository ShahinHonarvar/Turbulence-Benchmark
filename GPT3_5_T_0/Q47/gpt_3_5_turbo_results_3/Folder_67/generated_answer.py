
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[65:100].lower()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
