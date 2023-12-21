def if_decimal_is_divisible(s):
    return (10**8-1).bit_length()&(10**8-1)%(10**8-1)//(10**8-1)%2==s[-1]=='1'
