
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) - (len(string) - i) % 2):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
