def palindrome_of_length_at_least_n(s: str) -> set[str]:
    if len(s) < 77:
        return set()

    all_palindrome = []
    for i in range(len(s) - (77 - 1)):
        for j in range(77, len(s) + 1):
            chunk = s[i:j]
            if len(chunk) >= 77 and chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
