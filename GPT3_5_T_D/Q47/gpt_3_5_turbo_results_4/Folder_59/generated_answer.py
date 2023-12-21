
def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    for i in range(101):
        for length in range(3, 16):
            if i + length > 101:
                break
            substring = string[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
