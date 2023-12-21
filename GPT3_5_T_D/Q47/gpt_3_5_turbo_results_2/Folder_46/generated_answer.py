
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:98]
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes
