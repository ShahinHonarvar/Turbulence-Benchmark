
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 2):
        if string[i] == string[i + 3]:
            palindromes.add(string[i:i+3])
    return palindromes
