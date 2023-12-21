def palindrome_of_length_at_least_n(s):
    return {s[i:j] for i in range(0, len(s) - 1) for j in range(i, len(s) - 1) if s[i:j] == s[j:i] and s[i:j].lower() in 'qwertyuiopasdfghjklzxcvbnm' and len(s[i:j]) > 60}
