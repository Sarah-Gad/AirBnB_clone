#!/usr/bin/python3
"""This module will be the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """This is a sub class of the cmd class
    that will make the cmdloop"""
    prompt = "(hbnb)"
    __aval_clas = {
            "BaseModel"
    }

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

    def do_create(self, argyy):
        """This method is used to create a new instance"""
        if (len(argyy) == 0):
            print("** class name missing **")
            return
        try:
            created_ins = eval(argyy + "()")
            created_ins.save()
            print(created_ins.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, argyy):
        """This method will print the string representaion of the inst"""
        div_arg = argyy.split()
        serd_objs = storage.all()
        if (len(div_arg) == 0):
            print("** class name missing **")
        elif (div_arg[0] not in HBNBCommand.__aval_clas):
            print("** class doesn't exist **")
        elif (len(div_arg) == 1):
            print("** instance id missing **")
        elif ("{}.{}".format(div_arg[0],div_arg[1]) not in serd_objs):
            print("** no instance found **")
        else:
            print(serd_objs["{}.{}".format(div_arg[0],div_arg[1])])

    def do_destroy(self, argyy):
        """This method will be used to delete an instance"""
        div_arg = argyy.split()
        serd_objs = storage.all()
        if (len(div_arg) == 0):
            print("** class name missing **")
        elif (div_arg[0] not in HBNBCommand.__aval_clas):
            print("** class doesn't exist **")
        elif (len(div_arg) == 1):
            print("** instance id missing **")
        elif ("{}.{}".format(div_arg[0],div_arg[1]) not in serd_objs):
            print("** no instance found **")
        else:
            del serd_objs["{}.{}".format(div_arg[0],div_arg[1])]

    def do_all(self, argyy):
        """This method will give you the str representation of all instances"""
        div_args = argyy.split()
        if len(div_args) > 0 and div_args[0] not in HBNBCommand.__aval_clas:
            print("** class doesn't exist **")
        else:
            returned_st = []
            for f_inst in storage.all().values():
                if len(div_args) > 0 and div_args[0] == f_inst.__class__.__name__:
                    returned_st.append(f_inst.__str__())
                elif len(div_args) == 0:
                    returned_st.append(f_inst.__str__())
            print(returned_st)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

