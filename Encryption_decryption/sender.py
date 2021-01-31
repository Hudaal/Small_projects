from affine import affine
from caesar import caesar
from multiplikasjons_cypher import multiplikasjons_cypher
from person import person
from receiver import receiver
from rsa import rsa
from hacker import hacker
from ubrytelige import ubrytelige


class sender(person):
    def __init__(self, cypher_alg):
        super().__init__(cypher_alg)
        self.receiver = receiver(cypher_alg)

    def set_receiver(self, cypher_alg, receiver, key=False):
        keys_list = cypher_alg.generate_key(key)
        print(key)
        #print("list: {}".format(keys_list))
        self.key = keys_list[0]
        self.receiver = receiver
        self.receiver.set_key(keys_list[1])

    def operate_cypher(self, text):
        code = self.cypher_alg.encode(text, self.key)
        #decoded_code = self.receiver.operate_cypher(code)
        return code


def main():
    print("1)Caesar\n2)Multiplication\n3)affine\n4)ubrytelig\n5)rsa\n")
    which_alg = input(": ")
    if which_alg == '1':
        cy_alg = caesar()
    elif which_alg == '2':
        cy_alg = multiplikasjons_cypher()
    elif which_alg == '3':
        cy_alg = affine()
    elif which_alg == '4':
        cy_alg = ubrytelige()
    else:
        cy_alg = rsa()
    send = sender(cy_alg)
    receiv = receiver(cy_alg)
    hack = hacker(cy_alg)
    while True:
        choos_key = input(
            "Choose 1 to inter your key, else choose other number: ")
        if choos_key == '1':
            key = input("your key is: ")
            if which_alg == '4':
                send.set_receiver(cy_alg, receiv, key)
            elif which_alg == '3':
                key2 = input("your second key is: ")
                send.set_receiver(cy_alg, receiv, (int(key),int(key2)))
            else:
                send.set_receiver(cy_alg, receiv, int(key))
        else:
            send.set_receiver(cy_alg, receiv)
        receiv.set_sender(cy_alg, send)
        my_text = input("Your Text: ")
        code = send.operate_cypher(my_text)
        print("Cypher: " + code)
        decoded_code = receiv.operate_cypher(code)
        print("after: " + decoded_code)
        verify = cy_alg.verify(my_text, decoded_code)
        if verify:
            break
        else:
            print("Repeat!\n")
    print("hack: {} ".format(hack.hack(code)))


main()
