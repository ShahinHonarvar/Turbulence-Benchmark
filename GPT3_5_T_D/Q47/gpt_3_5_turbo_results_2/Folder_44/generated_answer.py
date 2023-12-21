

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[18:99].lower()
    for i in range(len(substring)):
        for j in range(31, 52):
            if i+j <= len(substring):
                palindrome = substring[i:i+j]
                if palindrome == palindrome[::-1] and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes
