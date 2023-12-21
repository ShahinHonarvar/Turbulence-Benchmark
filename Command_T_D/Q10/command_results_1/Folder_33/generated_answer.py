import re
def all_odd_ints_exclusive(nums):
    s = ''.join(str(n) for n in nums)
    m = re.match(r'( odd)?( int)?( exclusive)?', s)
    if m:
        s = m.group(0)
        if s[0] == 'odd':
            if s[1] == 'int':
                s += '?'
            else:
                s += ' int?'
        if s[2] == 'exclusive':
            s += '?'
        return nums[ 369 : 983 + 1 ] if nums[ 369 ] % 2 == 1 and nums[ 983 ] % 2 == 1 else []
