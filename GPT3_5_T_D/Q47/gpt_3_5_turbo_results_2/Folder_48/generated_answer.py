
def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[155:284]

    palindromes = set()
    for length in range(104, 121):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start+length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)

    return palindromes
