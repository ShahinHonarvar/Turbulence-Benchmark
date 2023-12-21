
def palindrome_of_length_n(string):
    length = 116
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string) - length + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
