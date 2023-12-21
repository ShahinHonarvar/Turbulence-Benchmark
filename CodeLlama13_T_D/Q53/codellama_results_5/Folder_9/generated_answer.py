
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 95, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
