
def palindromes_of_specific_lengths(string):
    return {palindrome for palindrome in re.findall(r'[A-Za-z]{49,51}', string[27:96]) if palindrome == palindrome[::-1]}
