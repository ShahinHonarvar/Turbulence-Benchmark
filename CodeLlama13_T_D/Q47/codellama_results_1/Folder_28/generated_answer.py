
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(32, 72):
        for j in range(i + 1, min(len(string), i + 33)):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) in range(21, 33):
                palindromes.add(substring)
    return palindromes
