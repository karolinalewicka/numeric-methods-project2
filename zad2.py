def is_palindrome(text):
    len_of_text = len(text)
    for i in range(len_of_text//2 + 1):
        if text[i] != text[len_of_text - i - 1]:
            return False
    return True
assert is_palindrome("ABA")

def are_letters_different(text):
    occurences = {}
    for letter in text:
        occurences[letter] = True
    return len(occurences.keys()) > 1

assert not are_letters_different("BBB")
assert are_letters_different("ABA")


def find_palindrome(text):
    for i in range(len(text) - 1):
        for j in range(i + 1):
            to_check = text[j:len(text)-i +j + 1]
            if is_palindrome(to_check) and are_letters_different(to_check):
                return to_check
    return "brak"


assert find_palindrome("CABA") == "ABA"
assert find_palindrome("CABCBABBB") == "ABCBA"
assert find_palindrome("CABCABBB") == "brak"

print(find_palindrome("ABABACA"))


