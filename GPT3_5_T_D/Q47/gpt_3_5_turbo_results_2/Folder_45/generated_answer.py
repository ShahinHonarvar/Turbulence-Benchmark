
def palindromes_of_specific_lengths(string):
    string = string.lower()[70:141]
    palindromes = set()
    for length in range(3, 61):
        for index in range(len(string) - length + 1):
            substring = string[index:index+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
