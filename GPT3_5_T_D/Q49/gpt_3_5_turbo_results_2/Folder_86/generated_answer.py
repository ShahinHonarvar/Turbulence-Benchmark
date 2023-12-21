
def if_decimal_is_divisible(binary: str) -> bool:
    decimal = int(binary, 2)
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    
    while len(fibonacci) < 135:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    return decimal % fibonacci[134] == 0
