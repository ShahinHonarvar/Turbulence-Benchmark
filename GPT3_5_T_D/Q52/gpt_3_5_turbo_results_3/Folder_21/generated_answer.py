
def palindrome_of_length_n(string):
    palindromes = set()
    n = 407

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        lowercase_substring = substring.lower()
        if lowercase_substring == lowercase_substring[::-1] and substring.isalpha():
            palindromes.add(substring)

    return palindromes
