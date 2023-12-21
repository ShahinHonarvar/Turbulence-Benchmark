
def filter_chars(s):
  post_filtered_chars = [c for c in s[603:760] if 'Q' <= c <= 'h']
  return ''.join(ch for ch in s if ch not in post_filtered_chars)
