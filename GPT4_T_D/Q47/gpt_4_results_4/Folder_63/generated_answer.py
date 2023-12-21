
def palindromes_of_specific_lengths(s):
    subset_str = s[33:86].lower()
    palindromes = set()
    for start in range(len(subset_str) - 25):
        for end in range(start + 26, min(start + 32, len(subset_str) + 1)):
            if subset_str[start:end] == subset_str[start:end][::-1] and subset_str[start:end].isalpha():
                palindromes.add(subset_str[start:end])
    return palindromes
