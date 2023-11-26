string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# This is an isomorphic checker
# Which means, "to map" a char to another
# egg -> add | e->a, g->d

def is_isomorphic(s1: str, s2: str) -> bool:

    if not len(s1) == len(s2):
        print("Not isomorphic because the string lenghts are different")
        return False

    # Make a dict, that will act as a 'key'
    isomorphic_key: dict[str] = {}
    for charX, charY in zip(s1, s2):
        isomorphic_key[charX] = charY

    # Now, try to get the origional value from the 'key'
    new_s2 = ""
    for charX in s1:
        new_s2 += isomorphic_key[charX]
    # Now, check if the new_s2 is equal to s2
    if new_s2 == s2:
        print("Isomorphic!")
        return True
    print("Not isomorphic")
    return False


def is_isomorphic2(s1: str, s2: str) -> bool:
    if not len(s1) == len(s2):
        print("Not isomorphic because the string lenghts are different")
        return False

    # Make a dict, that will act as a 'key'
    isomorphic_key: dict[str] = {}
    for charX, charY in zip(s1, s2):
        if isomorphic_key.get(charX) is None:
            isomorphic_key[charX] = charY

        elif isomorphic_key.get(charX) != charY:
            return False

    return True

def print_isomorphic_relation(s1: str, s2: str):
    # Make a dict, that will act as a 'key'
    isomorphic_key: dict[str] = {}
    for charX, charY in zip(s1, s2):
        isomorphic_key[charX] = charY

    print("Isomorphic relation: ")
    for key, value in isomorphic_key.items():
        print(key, "->", value)



if is_isomorphic2(string1, string2):
    print_isomorphic_relation(string1, string2)
else:
    print("Not isomorphic")

