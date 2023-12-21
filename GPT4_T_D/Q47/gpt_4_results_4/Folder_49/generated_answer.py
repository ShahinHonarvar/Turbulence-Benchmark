
def palindromes_of_specific_lengths(str):
    str = str[10:101]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(str) - length + 1):
            substring = str[i:i+length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes
