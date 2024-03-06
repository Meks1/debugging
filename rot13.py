
# Mērķis: 
# šifrēt tekstu ROT13 kodējumā


def rot13(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = alphabet.index(char)
            if is_upper:
                new_index = (char_index + 13) % 26 
                result += alphabet[new_index]
            else:
                new_index = (char_index + 13) % 26 + 26
                result += alphabet[new_index] 
        else:
            result += char

    return result

print("Enter a text to ROT13 encode")
text = input()
encrypted_text = rot13(text)
print("ROT13 Encoded Text:", encrypted_text)

# Kādas kļūdas izdevies atrast?
# incorrect syntax
