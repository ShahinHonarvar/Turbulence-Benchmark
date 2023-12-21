
def palindromes_of_specific_lengths(s):
    import re
    sub_str = s[10:76]
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 9, i + 21):
            if j < len(sub_str):
                possible_palindrome = sub_str[i:j+1]
                if possible_palindrome == possible_palindrome[::-1] and re.match("^[A-Za-z]*$", possible_palindrome):
                    palindromes.add(possible_palindrome.lower())
    return palindromes
