def palindrome_of_length_at_least_n(s: str) -> set[str]:
    if len(s) < 115:
        return set()

    all_palindrome = []
    for i in range(len(s) - (115 - 1)):
        for j in range(115, len(s) + 1):
            chunk = s[i:j]
            if len(chunk) >= 115 and chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
