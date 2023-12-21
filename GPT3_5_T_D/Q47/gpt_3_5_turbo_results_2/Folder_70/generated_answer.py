
def palindromes_of_specific_lengths(string):
    string = string[10:71]
    string = ''.join(filter(str.isalpha, string)).lower()

    palindromes = set()
    for length in range(24, 53):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
