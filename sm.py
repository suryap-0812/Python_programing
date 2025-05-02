# 

# help("topics")
# help("modules packages")
# help("print")

import instaloader
import os   
ig = instaloader.Instaloader()  
# ig.login("username", "password") # login to your account
ig.download_profile("itz_.sasi._xz", profile_pic_only=True) # download profile picture of the user
