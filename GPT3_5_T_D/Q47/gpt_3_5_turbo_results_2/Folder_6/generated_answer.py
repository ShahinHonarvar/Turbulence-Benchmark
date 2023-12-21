
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(45, 99):
        substring = string[i:i+47]
        for length in range(40, 48):
            if len(substring) >= length and substring.isalpha():
                palindrome = substring[:length]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes
