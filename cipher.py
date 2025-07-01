from random import randint
number = randint(0,26)
text = input('Enter the text to encrypt:\n')

def caesar(a, b):
    alpbhabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for i in a.lower():
        if i == ' ':
            encrypted_text += i
        else:
            c = alpbhabet.find(i)
            d = (c + b) % len(alpbhabet)
            encrypted_text += alpbhabet[d]
    print('plain message:', a)
    print('encrypted text:', encrypted_text)

caesar(text, number)
print('encrypted forward by', number)