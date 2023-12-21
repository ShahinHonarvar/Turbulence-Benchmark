
def palindromes_of_specific_lengths(s):
    substring = s[30:96]
    palindrome_characters = set()
    for i in range(len(substring)):
        for j in range(i+34, min(i+56, len(substring)+1)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindrome_characters.add(substring[i:j].lower())
    return palindrome_characters
