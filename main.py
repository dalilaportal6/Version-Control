'''
Lab 6 Verison Control
Author: Dalila Portal, Emma Baumgartner
Class: COP3502C
Section:12309
Description: A simplified password encoder/decoder program
'''

# Dalila Portal
def encode(password_string): # Encodes the passowrd by adding 3 to each of the numbers in the password
    encode_password = ''
    for i in password_string:
        encode_value = (int(i) + 3) % 10 # Loops it back so it doesn't surpass 9 and become a 2 digit number
        encode_password += str(encode_value)
    return encode_password

def decode_password(password_string):
    decode_password = []
    for digit in password_string:  # for char in len(0, len(password)
        if digit.isdigit():
            decode_password.append(str(int(digit) - 3))
    return ''.join(decode_password)

def menu():
    while True: # Loops menu if you don't exit
        print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit")
        user_input = input("\nPlease enter an option: ")
        if user_input == "1":
            user_password = input("Please enter your password to encode: ")
            encoded_result = encode(user_password) # Stores the encoded function
            print("Your password has been encoded and stored!\n")
        if user_input == "2": # Prints encoded password and then decodes it to print it as well
            decoded_result = decode_password(encoded_result)
            print(f"The encoded password is {encoded_result}, and the original password is {decoded_result}.\n")
        if user_input == "3":
            break # Exits

if __name__ == '__main__':
    menu()


