
def palindromes_of_specific_lengths(string):
    string = string.lower()
    string = string[11:97]
    palindromes = set()

    for length in range(45, 53):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)

    return palindromes
