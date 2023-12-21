
def palindromes_of_specific_lengths(string):
    substring = string[27:78]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 20, len(substring) + 1)):
            temp = substring[i:j]
            if temp == temp[::-1] and temp.isalpha():
                result.add(temp.lower())
    return result
