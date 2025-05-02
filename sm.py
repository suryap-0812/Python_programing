# # 

# # help("topics")
# # help("modules packages")
# # help("print")

# # import instaloader
# # import os   
# # ig = instaloader.Instaloader()  
# # # ig.login("username", "password") # login to your account
# # ig.download_profile("itz_.sasi._xz", profile_pic_only=True) # download profile picture of the user


# import pywhatkit

# pywhatkit.sendwhatmsg_instantly("+917010791279", "Hello, this is a test message!") # send a message to the number at 3:00 PM


class supermarket: # creatng a class named supermarket
    pname = input("Enter the product name: ") # taking input from user for product name
    qnty = int(input("Enter the quantity: ")) # taking input from user for quantity
    price = float(input("Enter the price: ")) # taking input from user for price

s = supermarket() # creating an object of the class supermarket
print("Product name: ", s.pname) # printing the product name
print("Quantity: ", s.qnty) # printing the quantity 
print("Price: ", s.price) # printing the price
print("Total price: ", s.qnty * s.price) # printing the total price by multiplying quantity and price



