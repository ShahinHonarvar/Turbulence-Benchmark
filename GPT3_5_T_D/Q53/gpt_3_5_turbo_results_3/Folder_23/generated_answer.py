
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 19, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
