
def palindromes_of_specific_lengths(s):
    import re
    s_substring = s[11:94]
    s_clean = re.findall(r'\b\w+\b', s_substring)
    palindromes = set()

    for sub_string in s_clean:
        if (34 <= len(sub_string) <= 54) and (sub_string.lower() == sub_string.lower()[::-1]):
            palindromes.add(sub_string)

    return palindromes
