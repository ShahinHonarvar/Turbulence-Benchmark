
def palindromes_of_specific_lengths(string):
    substring = string[22:96]
    substring = substring.lower()
    string_set = set()
    for length in range(52, 56):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start+length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                string_set.add(palindrome)
    return string_set
