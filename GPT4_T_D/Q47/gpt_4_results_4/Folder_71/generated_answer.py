
def palindromes_of_specific_lengths(s):
    import re
    start, end = 18, 66
    min_len, max_len = 23, 36
    s = s[start:end]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+min_len, min(i+max_len+1, len(s)+1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                cleaned_substring = re.sub("[^a-zA-Z]+", "", substring)
                if len(cleaned_substring) >= min_len:
                    palindromes.add(cleaned_substring)
    return palindromes
