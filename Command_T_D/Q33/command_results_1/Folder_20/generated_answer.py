def return_vowels(s):
    if not s:
        return []
    else:
        return [c for c in s[59:-1] if c.lower() in 'aeiouAEIOU']
