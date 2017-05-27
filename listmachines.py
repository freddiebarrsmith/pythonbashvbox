import subprocess
import os
import re

class Machine(object):

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid

    def printuuid(self):
        print self.uuid

    def printname(self):
        print self.name


    def startvm(self):
        subprocess.call(["VBoxManage", "startvm", self.name])

    def stopvm(self):
        subprocess.call(["VBoxManage", "poweroff", self.name])

vmarray = []


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
    vmarray.append(Machine(name, uuid))
    print name

menuselect = raw_input("Which machine do you want to run ?(enter number)")
menuselect = int(menuselect)
vmarray[menuselect-1].printname()

#potentially clone before running
#subprocess.call(["VBoxManage", "startvm", selectedvm ])
