def palindrome_of_length_at_least_n(s: str) -> set[str]:
    if len(s) < 95:
        return set()

    all_palindrome = []
    for i in range(len(s) - (95 - 1)):
        for j in range(95, len(s) + 1):
            chunk = s[i:j]
            if len(chunk) >= 95 and chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
