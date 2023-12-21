
def palindromes_of_specific_lengths(string):
    string = string[65:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
