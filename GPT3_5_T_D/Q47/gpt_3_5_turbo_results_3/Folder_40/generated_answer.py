
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(6):
        for j in range(i + 3, 6):
            substring = string[i:j+1]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
