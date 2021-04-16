def main():
    print("Выберите вариант: шифрование - encrypt, дешифрование - decrypt:")
    user_select = input().strip()
    if user_select == "encrypt":
        user_encrypt_text = input("Введите текст для шифрования:")
        user_encrypt_key = int(input("Введите ключ/сдвиг шифрования:"))
        print(encrypt(user_encrypt_text, user_encrypt_key))
    elif user_select == "decrypt":
        user_decrypt_text = input("Введите текст для дешифрования:")
        user_decrypt_key = int(input("Введите ключ/сдвиг дешифрования:"))
        print(decrypt(user_decrypt_text, user_decrypt_key))
    else:
        print("Неверно выбран режим")


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


if __name__ == "__main__":
    main()
