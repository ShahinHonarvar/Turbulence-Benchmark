
def palindrome_of_length_at_least_n(string):
    string = ''.join(filter(str.isalpha, string)).lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+46, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
