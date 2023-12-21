
def palindromes_of_specific_lengths(string):
    string = string[18:89]
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 12):
        substring = string[i:i+12]
        if substring == substring[::-1]:
            palindromes.add(substring)
    for i in range(len(string) - 13):
        substring = string[i:i+13]
        if substring == substring[::-1]:
            palindromes.add(substring)
    for i in range(len(string) - 14):
        substring = string[i:i+14]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
