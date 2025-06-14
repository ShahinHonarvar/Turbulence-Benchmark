
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(16, 60+1):
        for j in range(i-15, i+40):
            if string[j] == string[j].lower():
                continue
            substring = string[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
