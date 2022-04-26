sequence = "ABC"

def letter_to_binary(letter):
    n = ord(letter)
    array = []
    while n > 0:
        array.insert(0, str(n%2))
        n = n // 2
    txt =  "".join(array)
    txt = '0' * (8 - len(txt)) + txt
    return txt

def negate(txt):
    convert = lambda x: '0' if x == '1' else '1'
    return "".join([convert(x) for x in txt])


def test_scenario():
    assert letter_to_binary("B") == "01000010"
    assert letter_to_binary("A") == '01000001'
    assert negate('01000001') ==  "10111110"



def binary_to_letter(bin):
    decimal = 0 
    for i in bin: 
        decimal = decimal*2 + int(i) 
    return chr(decimal)

def test_bin_to_letter():
    assert binary_to_letter("01000001") == "A"

def scenario(letter):
    return binary_to_letter(negate(letter_to_binary(letter)))


if __name__ == '__main__':
    print(scenario('A'))
