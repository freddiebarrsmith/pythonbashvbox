import subprocess
import os
import re
import time

#class list(object):

class Machine(object):

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid
        self.clonename = name + str("cloned")

    def printuuid(self):
        print self.uuid

    def printname(self):
        print self.name

    def printclonename(self):
        print self.clonename

    def startvm(self):
        subprocess.call(["VBoxManage", "startvm", self.clonename])

    def stopvm(self):
        subprocess.call(["VBoxManage", "controlvm", self.clonename, "poweroff"])

    def clonevm(self):
        subprocess.call(["VBoxManage", "clonevm", self.name, "--name", self.clonename, "--register"])

    def deleteclone(self):
        subprocess.call(["VBoxManage", "unregistervm", self.clonename, "--delete"])


class Linux(Machine):
    def __init__(self, name, uuid):
        Machine.__init__(self, name, uuid)



class Windows(Machine):
    def __init__(self, name, uuid):
        Machine.__init__(self, name, uuid)


    def copyto(self):
        subprocess.call(["VBoxManage", "startvm", self.name])

    def copyfrom(self):
        subprocess.call(["VBoxManage", "startvm", self.name])

    def createdir(self):
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "createdir", "c://test", "--username", "pseudonym", "--password", "shifty"])
#vboxmanage guestcontrol windowsxpcloned createdir "c://test2" --username pseudo --password shifty
#vboxmanage guestcontrol windowsxpcloned createdir "c://test2" --username pseudonym --password shifty

           #vboxmanage guestcontrol windowsxp createdir "c://test2" --username pseudo --password shifty


            # vboxmanage guestcontrol "windowsxpcloned" copyto "/home/freddie/pythonbashvbox/testcopy.txt"
            ## --target-directory "C:/test/" --username pseudo --password shifty --verbose


#VBoxManage unregistervm  --delete

vmarray = []
clonearray = []

#http://www.saltycrane.com/blog/2011/04/how-use-bash-shell-python-subprocess-instead-binsh/
#os.system()
#def bash_command(cmd):
#    subprocess.Popen(cmd, shell=True, executable='/bin/bash')

#bash_command('VBoxManage list vms')

#subprocess.call(["VBoxManage", "list", "vms"])
strings = subprocess.check_output(["VBoxManage", "list", "vms"])
#print(strings)
#print type(strings)
for line in strings.splitlines():
    indexoffirstbracket = line.index('{')
    indexofsecondbracket = line.index('}')
    uuid = line[indexoffirstbracket+1:indexofsecondbracket]
    print uuid
    line = line[1:]
    indexofsecondquote = line.index('\"')
    name = line[:indexofsecondquote]
    vmarray.append(Windows(name, uuid))
    print name

menuselect = raw_input("Which machine do you want to run ?(enter number)")
menuselect = int(menuselect)
vmarray[menuselect-1].printuuid()
vmarray[menuselect-1].printuuid()



#
vmarray[menuselect-1].deleteclone()

vmarray[menuselect-1].clonevm()

time.sleep(10)
vmarray[menuselect-1].startvm()
time.sleep(90)

vmarray[menuselect-1].createdir()
time.sleep(30)
vmarray[menuselect-1].stopvm()

vmarray[menuselect-1].deleteclone()


#vmarray[menuselect-1].stopvm()

#potentially clone before running
#subprocess.call(["VBoxManage", "startvm", selectedvm ])
