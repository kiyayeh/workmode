"""
Author: Shy Stuart
Mail  : kiyashy@gmail.com
"""
# import liabery
import re

url = ["127.0.0.1 www.facebook.com",
       "127.0.0.1 www.yahoo.com.tw",
       "127.0.0.1 www.yahoo.com",
       "106.185.47.91 docs.lyrasoft.net"
       "127.0.0.1 ptt.cc"]



class WorkMode(object):

    #init
    def __init__ (self):
        self.path = '/etc/hosts'
        self.document = ""
        self.status = ""


    #file system open

    def loadfile(self):
        string = ""
        with open(self.path) as input:
            self.origin = input
            for i in input:
                string += str(i)
        self.document = string

    # find if it contains www.facebook.com
    def find_status(self):
        find = re.search(r"facebook", self.document.lower())
        if (find != None):
            self.status = "On"
        else:
            self.status = "Off"
            print find


	# if yes ? ask if want to turn off work mode
    def go(self):
        ans = ""
        if (self.status == "On"):
            ans = raw_input('Would you like to turn off the WorkMode? (y/n)')
            if (ans == "y"):
                self.delete()
                print bcolors.OKGREEN + "WorkMode : OFF" + bcolors.ENDC
            elif (ans == "n"):
                return 0
            else:
                self.go()
	# if not ? ask if want to turn on work mode
        if (self.status == "Off"):
            ans = raw_input('Would you like to turn on the WorkMode? (y/n)')
            if (ans == "y"):
                self.create()
                print  bcolors.OKGREEN + "WorkMode : ON"+ bcolors.ENDC
            elif (ans == "n"):
                return 0
            else:
                self.go()

    def create(self):
        """
        Write block site urls into hosts file
        """

        file_text = open(self.path, 'w')
        file_text.write(self.document)
        file_text.write("\n"+"127.0.0.1 www.facebook.com")
        file_text.write("\n"+"127.0.0.1 www.yahoo.com")
        file_text.write("\n"+"127.0.0.1 tw.yahoo.com")
        file_text.write("\n"+"106.185.47.91 docs.lyrasoft.net")
        file_text.close()

    def delete(self):
        """
        Delete block site urls from hosts file
        """
        #Read files and store in temp
        f = open(self.path, "r")
        lines = f.readlines()
        f.close()
        #Write temp into file if not contians forbidan urls
        f = open(self.path, 'w')
        for line in lines:
            if (line != "127.0.0.1 www.facebook.com" + "\n" and line != "127.0.0.1 www.yahoo.com" + "\n" and line != "127.0.0.1 tw.yahoo.com" + "\n" and line != "106.185.47.91 docs.lyrasoft.net"):
                f.write(line)
        f.close()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# execute
mode =  WorkMode()
mode.loadfile()
mode.find_status()
print bcolors.HEADER+ "Current WorkMode Status:  " + mode.status + bcolors.ENDC
mode.go()
