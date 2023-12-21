
import bisect

def return_binary_or_hexa(s):
    if s:
        a, b = s[0], s[-1]
        r = sum(x for x in range(a + 1, b - 1) if bisect.bisect_left(s, x) > 0)
        if r & 1:
            return f'0b{r:b}'
        else:
            return f'0x{r:x}'
    else:
        return ''
