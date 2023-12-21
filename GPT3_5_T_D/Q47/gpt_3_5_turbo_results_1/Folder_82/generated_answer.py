
def palindromes_of_specific_lengths(string):
    string = string[3:301].lower()
    palindromes = set()
    for length in range(30, 301):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
