given_string = "BAABABAAABAAB"
wanted_string = "AAB"


def brute_force(given, wanted):
    len_of_given = len(given)
    len_of_wanted = len(wanted)

    array_of_indexes = []

    for i in range (len_of_given - len_of_wanted + 1):
        left = given[i: i + len_of_wanted]
        if left != wanted:
            continue
        array_of_indexes.append(i)
    return array_of_indexes

print(brute_force(given_string, wanted_string))


assert brute_force(given_string, wanted_string) == [1, 7, 10]