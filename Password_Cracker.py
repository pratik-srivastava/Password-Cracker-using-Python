from random import *
import os
user_pass = input("Enter a password(password should not contain capital letters): ")
password = ['a','b','c','d','e','f','g','h','i','j','1','2','3','4','5','6']
pswd = ""
while(pswd != user_pass):
    pswd = ""
    for i in range(len(user_pass)):
        guess = password[randint(0,15)]
        pswd = str(guess) + str(pswd)
    print(pswd)
    print("Cracking Password.....Please Wait!")
    os.system("cls")

print("Your password is :",pswd)