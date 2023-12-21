
def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[33:86].lower()
    for n in range(26, 32):
        for i in range(len(substring)-n+1):
            if substring[i:i+n] == substring[i:i+n][::-1] and substring[i:i+n].isalpha():
                result.add(substring[i:i+n])
    return result
