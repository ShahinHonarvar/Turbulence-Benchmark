
def palindrome_of_length_n(string):
    length = 72
    palindromes = set()
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if len(substr) == length and substr.isalpha():
            reverse_substr = ''.join(reversed(substr))
            if substr == reverse_substr:
                palindromes.add(substr)
    return palindromes
