
def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[24:98]
    valid_palindromes = set()
    for i in range(len(substring)):
        for j in range(i+10, min(i+37, len(substring)+1)):
            candidate = substring[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                valid_palindromes.add(candidate)
    return valid_palindromes
