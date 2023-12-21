
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)-71):
        substring = string[i:i+72]
        substring = ''.join(filter(str.isalpha, substring))
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes
