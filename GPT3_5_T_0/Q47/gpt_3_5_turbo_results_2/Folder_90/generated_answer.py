
def palindromes_of_specific_lengths(string):
    substring = string[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
