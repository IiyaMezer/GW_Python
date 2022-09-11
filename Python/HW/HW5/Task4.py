def encode(message):
    cipher = ""
    i = 0
    while i <= len(message) - 1:
        count = 1
        char = message[i]
        j = i
        while j < len(message) - 1:
            if char == message[j + 1]:
                count += 1
                j += 1
            else:
                break
        cipher = cipher + str(count) + char
        i = j + 1
    return cipher


def decode(cipher):
    message = ""
    count = ""
    for char in cipher:
        # если текущий символ -число, то добавляем его к счетчику
        if char.isdigit():
            count += char
        else:
            # итоговая распаковка
            message += char * int(count)
            count = ""
    return message

def read_text (filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text

def write_text (filename, message_to_write):
    f = open(filename, 'r+')
    f.write(message_to_write)
    f.close()

write_text("encoded_message.txt", encode(read_text("message.txt")))
write_text("decoded_message.txt", decode(read_text("encoded_message.txt")))