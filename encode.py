'''
Lab 6
Alexander F & Jacob F
'''

# encode function
def encode(input_string_pass):
    try:

        list_pass = []

        for i in input_string_pass:
            list_pass.append(i)

        encoded_list = []

        for i in list_pass:
            i = int(i)
            i += 3
            i = str(i)
            encoded_list.append(i)

        encoded = ''.join(encoded_list)
        print("Your password has been encoded and stored!")

        return encoded
    except:
        print("Error")

# decode function
def decode(encoded):
            
    try:
        
        list_pass = []

        for i in encoded:
            list_pass.append(i)

        decoded_list = []

        for i in list_pass:
            i = int(i)
            i -= 3
            i = str(i)
            decoded_list.append(i)
            
        decoded = ''.join(decoded_list)
        print(f'The encoded password is {encoded}, and the original password is {decoded}.')
        return decoded
    
    except:
        print("Error")

# main function 
def main():
    user_choice = None

    while user_choice != 3:

        print("Menu",
              "------------",
              "1. Encode",
              "2. Decode",
              "3. Quit", sep='\n')
        user_choice = int(input("\nPlease enter an option: "))

        if user_choice == 1:
            encoded = encode(input("Please enter your password to encode: "))

        elif user_choice == 2:
            decode(encoded)

        elif user_choice == 3:
            break


if __name__ == '__main__':
    main()