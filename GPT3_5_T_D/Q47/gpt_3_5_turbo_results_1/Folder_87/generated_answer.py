
def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    for i in range(11, 94):
        for length in range(34, 55):
            if i + length <= 94:
                substring = string[i:i+length]
                if substring == substring[::-1]:
                    if substring.isalpha():
                        palindromes.add(substring)
    return palindromes
