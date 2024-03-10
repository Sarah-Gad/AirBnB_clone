#!/usr/bin/python3
"""This module will be the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """This is a sub class of the cmd class
    that will make the cmdloop"""
    prompt = "(hbnb)"

    def do_quit(self, argyy):
        """I used this method to make a command that
        exits the command line interpreter"""
        return True

    def do_EOF(self, argyy):
        """I override this method to handle the
        case of reaching the end of file case"""
        return True

    def emptyline(self):
        """I override this method so thatif an emptyline
        is entered, this doesnt do anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

