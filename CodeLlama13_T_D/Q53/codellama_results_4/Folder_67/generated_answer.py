
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(25, len(string)):
        for j in range(len(string) - i + 1):
            if string[j:j+i] == string[j+i-1::-1]:
                palindromes.add(string[j:j+i])
    return palindromes
