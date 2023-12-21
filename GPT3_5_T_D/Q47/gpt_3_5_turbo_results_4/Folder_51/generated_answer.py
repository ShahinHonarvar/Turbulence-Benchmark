
def palindromes_of_specific_lengths(string):
    string = string[2:9].lower()
    palindromes = set()
    for i in range(3, 5):
        for j in range(len(string) - i + 1):
            substring = string[j:j+i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
