import os
import random
userNum = str(random.randrange(1,2000))
print("adduser user" + userNum)
os.system("sudo adduser user" + userNum)
os.system("su user" + userNum)