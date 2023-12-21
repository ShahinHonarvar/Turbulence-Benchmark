 def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 78):
        substr = s[i:i+79]
        if len(substr) == 79 and substr.isalpha():
            result.append(substr)

    return result
