def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 130, -1, -1):
        j = i
        while j < i + 130:
            if s[j] == s[j][::-1]:
                result.add(s[i:j + 1])
            j += 1
    return result
