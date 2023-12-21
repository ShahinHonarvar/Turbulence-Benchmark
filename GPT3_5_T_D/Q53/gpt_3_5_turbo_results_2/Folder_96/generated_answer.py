
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-23):
        for j in range(i+24, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
