
def palindromes_of_specific_lengths(string):
    return {palindrome for palindrome in re.findall(r'[A-Za-z]{4,5}', string[63:70]) if palindrome == palindrome[::-1]}
