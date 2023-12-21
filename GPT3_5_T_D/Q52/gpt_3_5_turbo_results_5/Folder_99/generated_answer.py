
def palindrome_of_length_n(string):
    palindromes = set()
    length = 420
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
