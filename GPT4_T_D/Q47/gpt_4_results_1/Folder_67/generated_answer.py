
def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    results=set()
    for length in range(26, 34):
        for i in range(len(s)-length+1):
            sub = s[i:i+length]
            if sub==sub[::-1] and sub.isalpha():
                results.add(sub)
    return results
