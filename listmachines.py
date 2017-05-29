import subprocess
import os
import re
import time
###prerequisites
###need to install guest additions on each host
###need to
###install python 2 on each target host
###run gpedit.msc and change security settings
#class list(object):

class Machine(object):

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid
        self.clonename = name + str("cloned")
        #add self.malwarename

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
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "copyto", "/home/freddie/pythonbashvbox/testcopy.txt", "--target-directory", "c://test", "--username", "pseudonym", "--password", "shifty"])

    def copyfrom(self):
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "createdir", "c://test", "--username", "pseudonym", "--password", "shifty"])

    def createmalwaredir(self):
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "createdir", "c://malware", "--username", "pseudonym", "--password", "shifty"])

    def createpcapsdir(self):
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "createdir", "c://pcaps", "--username", "pseudonym", "--password", "shifty"])


#    def runexe(self):
#        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "run", "--exe", "C://malware/sample.exe", "--wait-stdout", "--username", "pseudonym", "--password", "shifty"])

    def runexe(self):
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "run", "--exe", "C://malware/calc.exe", "--wait-stdout", "--username", "pseudonym", "--password", "shifty"])


    def copymalware(self):
        subprocess.call(["vboxmanage", "guestcontrol", self.clonename, "copyto", "/home/freddie/malware/calc.exe", "--target-directory", "c://malware", "--username", "pseudonym", "--password", "shifty"])

#https://www.virtualbox.org/wiki/Network_tips
#
# VBoxManage modifyvm [your-vm] --nictrace[adapter-number] on --nictracefile[adapter-number] file.pcap
    def listnics(self):
        print name
    def runpacketsniffer(self):
#        print name
        malwarename = "malware"
        pcapname = str(self.clonename) + str(malwarename) + str(".pcap")
        subprocess.call(["VBoxManage", "modifyvm", self.clonename, "--nictrace1", "on", "--nictracefile1", pcapname])

    def executemalware(self):
        print name
    #vboxmanage guestcontrol "windowsxpcloned" run --exe "C:/calc.exe"
    ## --wait-stdout --username "pseudonym" --password "shifty" --verbose


#vboxmanage guestcontrol "windowsxpclonedrun --exe "C:/calc.exe"
# --username "pseudonym" --password "shifty" --verbose





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



#vmarray[menuselect-1].runexe()
#
#vmarray[menuselect-1].deleteclone()
#vmarray[menuselect-1].deleteclone()

vmarray[menuselect-1].clonevm()
time.sleep(5)

vmarray[menuselect-1].runpacketsniffer()

time.sleep(10)
vmarray[menuselect-1].startvm()
time.sleep(60)
vmarray[menuselect-1].createmalwaredir()
time.sleep(5)

vmarray[menuselect-1].copymalware()
time.sleep(5)

vmarray[menuselect-1].runexe()
time.sleep(5)
#vmarray[menuselect-1].copyto()
print "copied"
time.sleep(30)
#vmarray[menuselect-1].stopvm()

#


#vmarray[menuselect-1].stopvm()

#potentially clone before running
#subprocess.call(["VBoxManage", "startvm", selectedvm ])
