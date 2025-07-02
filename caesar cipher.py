from random import randint
number = randint(0,26)
text = input('Enter the text to encrypt:\n')

def caesar(messgae, digit):
    alpbhabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for i in messgae.lower():
        if i == ' ':
            encrypted_text += i
        else:
            c = alpbhabet.find(i)
            d = (c + digit) % len(alpbhabet)
            encrypted_text += alpbhabet[d]
    print('plain message:', messgae)
    print('encrypted text:', encrypted_text)

caesar(text, number)
print('encrypted forward by', number)