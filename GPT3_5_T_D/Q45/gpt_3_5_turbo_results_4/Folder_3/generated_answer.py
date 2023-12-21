
def palindromes_between_indices(s):
    string = s[7:10].lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
