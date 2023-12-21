
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+24, len(s)+1):
            chunk = s[i:j]
            if chunk == chunk[::-1] and chunk.isalpha():
                result.add(chunk)
    return result
