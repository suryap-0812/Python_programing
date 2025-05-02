# # 

# # help("topics")
# # help("modules packages")
# # help("print")

# # import instaloader
# # import os   
# # ig = instaloader.Instaloader()  
# # # ig.login("username", "password") # login to your account
# # ig.download_profile("itz_.sasi._xz", profile_pic_only=True) # download profile picture of the user


import pywhatkit
# pywhatkit.sendwhatmsg_instantly("+917010791279", "Hello, this is a test message!") # send a message to the number at 3:00 PM


class supermarket: # creatng a class named supermarket
    def __init__(self):
       print("Welcome to the supermarket") # printing welcome message
    def sendmsg(self, mobile, info):
        print("Sending message to: ", mobile)
        pywhatkit.sendwhatmsg_instantly(self.st+mobile, info)
        print("Message: ", info)
    def select(self):
        a = input("Select the country:\n1. India\n2. USA\n3. UK\n")
        if a == "1":
            print("You have selected India")
            self.st = "+91"
        elif a == "2":
            print("You have selected USA")
            self.st = "+1"
        elif a == "3":
            print("You have selected UK")
            self.st = "+44"
        else:
            print("Invalid selection")
       
     
s = supermarket() # creating an object of the class supermarket
s.select()
s.sendmsg("9361526618", "hello bhaii")


