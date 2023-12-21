
def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string[13:100].lower()
    for i in range(len(string)):
        for j in range(i+26, min(i+30, len(string)+1)):
            substring = string[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
