
def palindromes_of_specific_lengths(string):
    substring = string[119:257]
    palindromes = set()
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes
