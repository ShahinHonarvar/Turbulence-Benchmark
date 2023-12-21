
def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    result = set()
    for length in range(24, 53):
        for i in range(len(s)-length+1):
            subset = s[i:i+length]
            if subset == subset[::-1] and subset.isalpha():
                result.add(subset)
    return result
