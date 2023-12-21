
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(103, 276 + 1):
        for j in range(i + 100, i + 169 + 1):
            substring = string[i:j]
            if len(substring) % 2 == 0 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
