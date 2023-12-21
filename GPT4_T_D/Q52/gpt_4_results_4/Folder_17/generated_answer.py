
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+289, len(s)+1):
            chunk = s[i:j]
            if chunk == chunk[::-1] and chunk.isalpha():
                results.add(chunk)
    return results
