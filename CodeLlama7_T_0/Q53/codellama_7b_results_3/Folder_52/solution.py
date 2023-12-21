def palindrome_of_length_at_least_n(s: str) -> set[str]:
    if len(s) < 14:
        return set()

    all_palindrome = []
    for i in range(len(s) - (14 - 1)):
        for j in range(14, len(s) + 1):
            chunk = s[i:j]
            if len(chunk) >= 14 and chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
