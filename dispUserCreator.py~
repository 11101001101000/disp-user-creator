import os
import random
import time
userNum = str(random.randrange(1,2000))
print("adduser disp" + userNum)
os.system("sudo adduser disp" + userNum)
print("Switching to created disp-user. Type disp" + userNum + "\'s password.")
os.system("su -l disp" + userNum)
os.system("sudo pkill -9 -u disp" + userNum)
time.sleep(0.5)
os.system("sudo userdel disp" + userNum)