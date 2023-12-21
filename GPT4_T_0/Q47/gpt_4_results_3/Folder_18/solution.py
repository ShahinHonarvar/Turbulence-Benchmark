def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[11:83 + 1]
    if len(s) < 13 or len(list(s)) == len(set(s)):
        return set()
    all_palindrome = []
    for k in range(13, 66 + 1):
        for i in range(0, len(s)):
            chunk = s[i:i + k]
            if len(chunk) < k:
                break
            if chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
