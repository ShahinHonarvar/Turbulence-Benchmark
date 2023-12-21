
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)-254):
        segment = s[i:i+255]
        if not segment.isalpha():
            continue
        if segment == segment[::-1]:
            result.add(segment)
    return result
