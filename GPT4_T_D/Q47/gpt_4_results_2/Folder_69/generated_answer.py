
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:97]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            substring = s[start:end]
            is_palindrome = substring.lower() == substring[::-1].lower()
            length = len(substring)
            contains_only_eng_letters = bool(re.fullmatch('[a-z]*', substring, re.I))
            if is_palindrome and 45 <= length <= 52 and contains_only_eng_letters:
                palindromes.add(substring)
    return palindromes
