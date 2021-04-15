def encrypt(text, key):
    symbols = '1234567890 .,?"!\'-'
    language = check_language(text)
    alphabet_length = get_language_alphabet_length(language)
    encrypted_text = ""
    for letter in text:
        if letter in symbols:
            encrypted_text += letter
            continue
        if letter.islower():
            start = get_starting_index_of_language(language)
        elif letter.isupper():
            if language == "english":
                start = 65
            else:
                start = get_starting_index_of_language(language) - alphabet_length
        encrypted_char_index = (ord(letter) - start + key) % alphabet_length + start
        encrypted_text += (chr(encrypted_char_index))
    return encrypted_text


def decrypt(encrypted_text, key):
    symbols = '1234567890 .,?"!\'-'
    language = check_language(encrypted_text)
    alphabet_length = get_language_alphabet_length(language)
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in symbols:
            decrypted_text += letter
            continue
        if letter.islower():
            start = get_starting_index_of_language(language)
        elif letter.isupper():
            if language == "english":
                start = 65
            else:
                start = get_starting_index_of_language(language) - alphabet_length
        decrypted_char_index = (ord(letter) - start - key) % alphabet_length + start
        decrypted_text += (chr(decrypted_char_index))
    return decrypted_text


def get_starting_index_of_language(language):
    if language.lower() == 'english':
        return 97
    elif language.lower() in 'russian':
        return 1072


def get_language_alphabet_length(language):
    if language == 'russian':
        return 32
    elif language == 'english':
        return 26


def check_language(string):
    ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    en = "abcdefghijklmnopqrstuvwxyz"

    string = [i for i in string if i.isalpha()]
    for letter in string:
        if letter.lower() not in ru:
            break
    else:
        return 'russian'

    for letter in string:
        if letter.lower() not in en:
            break
    else:
        return 'english'

print(encrypt("abcd", 2))