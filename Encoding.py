alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
should_Do = True
while should_Do is True:
    direction = input("Type encode to encrypt and decode to decrypt\n ").lower()
    text = input("give the message\n").lower()
    shift = int(input("give the number to shift the letter\n"))
    set1 = list(text)
    x3 = []


    def encode():
        for i in set1:
            if i == ' ':
                x3.append(" ")
            elif i not in alphabet:
                x3.append(i)
            else:
                x = int(alphabet.index(i))
                x1 = x + shift
                if x1 > 26:
                    x1 = x1 - 26
                else:
                    x1 = x1
                x2 = alphabet[x1]
                x3.append(x2)

        x4 = ' '.join(x3)
        print(x4)


    def decode():
        for i in set1:
            if i == ' ':
                x3.append(" ")
            elif i not in alphabet:
                x3.append(i)
            else:
                x = int(alphabet.index(i))
                x1 = x - shift
                x2 = alphabet[x1]
                x3.append(x2)

        x4 = ' '.join(x3)
        print(x4)


    if direction == "encode":
        encode()
        should_Do = input("Do you want to continue?\n")
        if should_Do == "yes":
            should_Do = True
        else:
            should_Do = False

    else:
        decode()
        should_Do = input("Do you want to continue?\n")
        if should_Do == "yes":
            should_Do = True
        else:
            should_Do = False
