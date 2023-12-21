import string


def palindrome_of_length_n(s: str) -> set[str]:
    if len(s) < 93:
        return set()
    all_palindrome = []
    for i in range(0, len(s)):
        chunk = s[i:i + 93]
        if len(chunk) < 93:
            break
        if chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
            all_palindrome.append(chunk)

    if len(all_palindrome) > 0:
        return set(all_palindrome)
    else:
        return set()
