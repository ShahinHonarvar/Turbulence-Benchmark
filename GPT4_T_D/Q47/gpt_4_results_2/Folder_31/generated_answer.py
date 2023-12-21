
def palindromes_of_specific_lengths(str):
    substring = str[11:84]
    result_set = set()
    for i in range(len(substring)):
        for j in range(i + 37, min(i + 61, len(substring) + 1)):
            word = substring[i:j]
            if word == word[::-1] and word.isalpha():
                result_set.add(word.lower())
    return result_set
