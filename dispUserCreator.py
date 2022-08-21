import os
import random
userNum = str(random.randrange(1,2000))
print("adduser disp" + userNum)
os.system("sudo adduser disp" + userNum)
os.system("su -l disp" + userNum)
os.system("sudo pkill -9 -u disp" + userNum)
os.system("sudo userdel disp" + userNum)