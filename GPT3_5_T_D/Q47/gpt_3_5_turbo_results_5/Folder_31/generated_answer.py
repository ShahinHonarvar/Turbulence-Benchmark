
def palindromes_of_specific_lengths(string):
    substring = string[11:84].lower()
    palindromes = set()
    for i in range(37, 61):
        for j in range(len(substring) - i + 1):
            if substring[j:j+i] == substring[j:j+i][::-1] and substring[j:j+i].isalpha():
                palindromes.add(substring[j:j+i])
    return palindromes
