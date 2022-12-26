#!/usr/bin/python3
'''Entry point of the command interpreter
'''
import cmd
import json
import re


def isfloat(s):
    '''Checks if a string is a decimal'''
    try:
        float(s)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    '''Shell for database
    '''

    prompt = '(hbnb) '
    model_list = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', "Place", "Review"
                  ]
    queries = ['all', 'count', 'show', 'destroy', 'update']

    @classmethod
    def handle_errors(cls, args: str, **kwargs):
        '''Error Handler for all commands'''

        if "all" in kwargs.values():
            if not args:
                return False

        if not args:
            print("** class name missing **")
            return True
        else:
            args = args.split(" ")

        n = len(args)

        if n < 1:
            print("** class name missing **")
            return True

        if args[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return True

        if 'command' not in kwargs:
            return False

        for _, arg in kwargs.items():
            if arg in ['create', 'show', 'destroy']:
                if n < 2:
                    print("** instance id missing **")
                    return True
            elif arg in ['update']:
                if n < 2:
                    print("** instance id missing **")
                    return True
                elif n < 3:
                    print("** attribute name missing **")
                    return True
                elif n < 4:
                    print("** value missing **")
                    return True
                elif n == 4 and args[2] == "":
                    print("** attribute name missing **")
                    return True

        return False

    def do_quit(self, args: str):
        '''Quit command to exit the program'''

        return True

    def do_EOF(self, args):
        '''EOF command to exit the program'''

        return True

    def do_create(self, args: str):
        '''
        Creates a new instance of a class, saves it to JSON
        file, prints the instance id
        Usage: create <class name>
        '''

        if HBNBCommand.handle_errors(args):
            return

        args = args.split(" ")
        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def do_show(self, args: str):
        '''
        Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <id>
               <class name>.show("<id>")
        '''

        if HBNBCommand.handle_errors(args, command='show'):
            return

        args = args.split(" ")
        objects = models.storage.all()
        key = ".".join(args)
        obj = objects.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, args: str):
        '''
        Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
               <class name>.destroy("<id>")
        '''

        if HBNBCommand.handle_errors(args, command='destroy'):
            return

        args = args.split(" ")
        objects = models.storage.all()
        key = ".".join(args)

        delete = False
        if key in objects and models.storage.delete(objects[key]):
            pass
        else:
            print("** no instance found **")

    def do_count(self, args: str):
        '''
        counts all string representation of all instances based
        or not on the class name.
        Usage: count <class_name>
               <class name>.count()
        '''

        if HBNBCommand.handle_errors(args):
            return

        args = args.split(" ")
        objects = models.storage.all()
        _all = []

        for k, v in objects.items():
            key = k.split(".")
            if key[0] == args[0]:
                _all.append(str(v))

        print(len(_all))

    def do_all(self, args: str):
        '''
        Prints all string representation of all instances based
        or not on the class name.
        Usage: all
               all <class name>
               <class name>.all()
        '''

        if HBNBCommand.handle_errors(args, command='all'):
            return

        args = args.split(" ")

        objects = models.storage.all()

        if args[0] == "":
            for obj in objects.values():
                print(obj)

        else:
            for key in objects:
                k = key.split(".")
                if k[0] == args[0]:
                    print(objects[key])
