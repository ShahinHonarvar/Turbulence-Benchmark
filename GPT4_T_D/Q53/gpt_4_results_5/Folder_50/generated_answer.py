
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = ''.join(c for c in string if c.isalpha()).lower()

    for i in range(len(string)):
        for j in range(i + 91, len(string) + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
