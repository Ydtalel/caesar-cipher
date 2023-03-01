from art import logo

go_on = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, encode_or_decode):
    result_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            result_text += alphabet[new_position]
        else:
            result_text += letter
    print(f"The {direction}d text is {result_text}")


print(logo)

while go_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, encode_or_decode=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if again == 'no':
        print("Goodbye!")
        go_on = False
