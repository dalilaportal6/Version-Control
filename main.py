'''
Lab 6 Verison Control
Author: Dalila Portal, Emma Baumgartner
Class: COP3502C
Section:12309
Description: A simplified password encoder/decoder program
'''

# Dalila Portal
def encode(password):
    encode_password = ''
    for i in password_string:
        encode_value = int(i) + 3
        encode_password += str(encode_value)
    return encode_password


def menu():
    while True:
        print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit")
        user_input = input("\nPlease enter an option: ")
        if user_input == "1":
            user_password = input("Please enter your password to encode: ")
            encoded_result = encode(user_password)
            print("Your password has been encoded and stored!\n")
        if user_input == "2":
            print(f"The encoded password is {encoded_result}, and the original password is {user_password}.\n")
        if user_input == "3":
            break

if __name__ == '__main__':
    menu()


