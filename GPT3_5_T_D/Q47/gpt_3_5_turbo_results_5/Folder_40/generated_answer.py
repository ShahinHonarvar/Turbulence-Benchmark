
def palindromes_of_specific_lengths(string):
    string = string[:6].lower()
    palindromes = set()
    for length in range(3, 6):
        for i in range(6 - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
