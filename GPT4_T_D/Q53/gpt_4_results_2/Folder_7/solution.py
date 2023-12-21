def palindrome_of_length_at_least_n(s: str) -> set[str]:
    if len(s) < 122:
        return set()

    all_palindrome = []
    for i in range(len(s) - (122 - 1)):
        for j in range(122, len(s) + 1):
            chunk = s[i:j]
            if len(chunk) >= 122 and chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
