import sys
import argparse
import platform
from os import *
from getpass import getuser

import colorama
from termcolor import cprint

def startConsole():
    colorama.init()
    print(platform.system(),platform.release(),'[Version '+platform.version()+']')
    print('Python',sys.version,'\n')

    while True:
        cmd = input(getdir()+'>')
        if cmd[-1] == ':':
            commands = cmd
            while True:
                command = input('...')
                if command == '':
                    break
                else:
                    commands+=('\n'+command)
            try:
                exec(compmands+'\n'+'')
            except Exception as e:
                cprint(e,'white','on_red',attrs=['bold'])
        else:
            try:
                output = eval(cmd)
                if output != None:
                    print(output)
            except:
                try:
                    exec(cmd)
                except Exception as e:
                    cprint(e,'white','on_red',attrs=['bold'])

cd = chdir;getdir = getcwd;deldir = rmdir;shell = system
del chdir;del getcwd;del rmdir;del system

cd('C:/Users/'+getuser())
startConsole()
