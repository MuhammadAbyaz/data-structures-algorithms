alphabets = [chr(i) for i in range(97, 123)]


def cipherText(text: str, key):
    ciphered_text = list()
    for i in text.lower():
        character = alphabets[(alphabets.index(i) + key) % 26]
        ciphered_text.append(character)
    return "".join(ciphered_text)


def decipherText(ciphered_text, key):
    plain_text = list()
    for i in ciphered_text.lower():
        character = alphabets[alphabets.index(i) - key % 26]
        plain_text.append(character)
    return "".join(plain_text)


print(decipherText(ciphered_text=cipherText("hello", 3), key=3))
