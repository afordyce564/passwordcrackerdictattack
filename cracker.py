#!C:\Program Files\Python312
import zipfile #library to extract zip files
import time    #library to control time spent in cracking process
import sys     #library to control arguments of the script
import re      #library to match password to patterns
#import exrex   #library to generate lists based on regex

zfile = sys.argv[1]
dfile = sys.argv[2]
filezip = zipfile.ZipFile(zfile) # We used the zipfile library to open the zipped file.
passFile = open(dfile) # We open the dictionary file.
count=0 #initializes count variable for for loop
start = time.time() #begins timer for the cracker

for line in passFile.readlines():
    password = line.strip("\n") #removing end of line
    codedpass = bytes(password, "utf-8") #password coded in binary
    #count = count + 1
    try: 
        filezip.extractall(pwd=codedpass) #trying password with zipfile library
    except:
        #print ("[-] Password not found. Attempted: " + str(count)
        #all of these statements attempt to match the password and increase count if found
        if re.match('\d{1}\d*', password):
            count = count + 1
        elif re.match('\D{1}\D*', password):
            count = count + 1
        elif re.match("[a-z]{1}[a-z]*", password):
            count = count + 1 
        elif re.match("[A-Z]{1}[A-Z]*", password):
            count = count +1
        elif re.match('[A-Z]{1}\w*\D*', password):
            count +=1
        elif re.match('[a-z]{1}\w*\D*', password):
             count +=1
        elif re.match('\D{1}\w*\D*', password):
            count += 1
        elif re.match('\d{1}\w*\D*', password):
            count += 1
        else: 
            #prints attempted password
            print(" ** Attempted ** "+ password)
    else:
        print("[------- Password Found -------] --> "+password)
        end = time.time() #ends timer for the cracker
        elapsed_time = end-start
        print("Time consumed: "+str(elapsed_time) + " seconds")
        print("Passwords attempted: "+ str(count)+". At "+str(count/elapsed_time) + " tries per second")
        exit(0)
        
#time to make a list of passwords
#this is the pattern I used to create task4.list
#print(list(exrex.generate("(peter|belinda|mario|pooja)(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])(0[0-9]|1[0-9]|2[0])")))