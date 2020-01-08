from random import SystemRandom
import time

def password_generator():
    try:
        length = int(input("> "))
        if length <= 15 or length >= 33: #valid the length (it will be used by AES method)
            print("Invalid length, try again")
            return password_generator()
        else:
            print("Please, wait a second")
            time.sleep(0.5) #this make it look cooler(?

            values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

            crypto_generator = SystemRandom() #Call SystemRandom class
            p = ""
            #int i = length; i > 0; i--
            for i in range(length,0,-1):
                p = p + crypto_generator.choice(values) #concatenate all the choices from values with "p"
            return p
    except ValueError:
        print("The entry must be a number, let´s try again :) ")

print("Password generated ", password_generator())
