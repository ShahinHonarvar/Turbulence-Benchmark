
def palindromes_of_specific_lengths(string):
    substring = string[3:301].lower()
    palindromes = set()
    for length in range(30, 301):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
