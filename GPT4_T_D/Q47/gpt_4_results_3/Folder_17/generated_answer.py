
def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[22:96]
    for i in range(len(substring)):
        for j in range(i+52, min(i+56, len(substring)+1)):
            phrase = substring[i:j]
            if phrase == phrase[::-1] and phrase.isalpha():
                result.add(phrase.lower())
    return result
