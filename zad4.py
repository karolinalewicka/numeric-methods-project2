# decimal to binary

def decimalToBinary(n):
    array = []
    while n > 0:
        array.insert(0, str(n%2))
        n = n // 2
    return "".join(array)
  


def test_decimal_to_binary():
    assert decimalToBinary(8) == '1000'
    assert decimalToBinary(18) == '10010'
    assert decimalToBinary(7) == '111'


# # Binary to decimal

def binaryToDecimal(bin):
    decimal = 0 
    for i in bin: 
        decimal = decimal*2 + int(i) 
    return decimal   


def test_binary_to_decimal():
    assert binaryToDecimal('100') == 4
    assert binaryToDecimal('10010') == 18
    breakpoint()
    assert binaryToDecimal('111') == 7

