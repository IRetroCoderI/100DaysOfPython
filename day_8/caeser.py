# day 8 project

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
    encrypted = []
    message = message.lower()
    for i in message:
        if i in alpha:
            shifted_position = alpha.index(i) + shift
            shifted_position %= len(alpha)
            encrypted.append(alpha[shifted_position])
                
        else:
            encrypted.append(i)
    final = ''.join(encrypted)
    return final

def decode(message, shift):
    message = message.lower()
    decrypted = []
    for i in message:
        if i in alpha:
            decrypted.append(alpha[alpha.index(i)-shift])
        else:
            decrypted.append(i)
    final = ''.join(decrypted)
    return final


user = ''
while user != 'no':
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if choice == 'encode':
        answer = encode(message, shift)
        print(f"Here's the encoded result: {answer}")
    elif choice == 'decode':
        answer = decode(message, shift)
        print(f"Here's the decoded result: {answer}")

    user = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if user == 'yes':
        continue
    


