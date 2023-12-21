
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        if len(string[i:]) < 41:
            continue
        palindrome = string[i:i+41]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
