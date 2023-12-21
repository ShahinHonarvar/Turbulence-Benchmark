
def palindrome_of_length_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        if len(string[i:i+n]) == n:
            if string[i:i+n].lower() == string[i:i+n][::-1].lower():
                palindromes.add(string[i:i+n])
    return palindromes
