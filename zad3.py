def any_letter_is_the_same(left, right):
    for letter in set(left):
        if letter in right:
            return True
    return False


def find_boyer_moore(text, pattern):
    index = len(pattern) -1
    while True:
        letter = text[index]
        if letter != pattern[-1]:
            if any_letter_is_the_same(text[index + 1 - len(pattern):index + 1], pattern):
                index = index + 1
            else:
                index = index + len(pattern)
        else:
            if text[index + 1 - len(pattern):index + 1] == pattern:
                return index - len(pattern) + 1
            index = index + 1
        if index >= len(text):
            return None

assert find_boyer_moore("nxbdhs", "bdh") == 2
assert find_boyer_moore("qwertyuhygfdsdfghfdsfg", "qwer") == 0
assert find_boyer_moore("qwadsdewxcefdsfg", "sfg") == 13
assert find_boyer_moore("qwgadsdewgxcefdsfg", "sfg") == 15