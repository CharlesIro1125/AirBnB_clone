#!/usr/bin/python3
"The console entry point"
import cmd
from models import storage
from models.base_model import BaseModel
import signal
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]

class HBNBCommand(cmd.Cmd):
    "A command line interface"

    prompt = '(hbnb) '
    intro = 'Cmd interpreter'
    _interrupted = False

    def __init__(self):
        signal.signal(signal.SIGINT, handler=self._ctrl_c_handler)
        super().__init__()

    def _ctrl_c_handler(self, signal, frame):
        print('')
        exit(0)

    def precmd(self, line):
        storage.reload()
        return cmd.Cmd.precmd(self, line)

    def do_EOF(self, line):
        "The EOF method returns true"
        if line:
            print("args passed")
        else:
            return True

    def do_create(self, line):
        "creates an instance of BaseModel"
        if line in CLASSES:
            lines = line.split(' ')
            new_model = eval(lines[0])()
            new_model.save()
            print(new_model.id)
        elif line == '':
            print('** class name missing **')
        elif line not in CLASSES:
            print("** class doesn't exist **")

    def do_exit(self, line):
        return True

    def do_quit(self, line):
        "The quit method returns True"
        if line:
            print("args passed(quit)")
        else:
            return True

    def emptyline(self):
        "method called when an empty line is entered"
        "to the prompt"
        return cmd.Cmd.emptyline(self)

    def do_destroy(self, line):
        "delete an instance"
        if line == '':
            print('** class name missing **')
        else:
            lines = line.split(' ')
            if len(lines) > 0 and lines[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(lines) == 1:
                print("** instance id missing **")
            elif len(lines) > 1 and lines[0] in CLASSES:
                all_instance = storage.all()
                idx = "{0}.{1}".format(lines[0],lines[1])
                if idx not in all_instance.keys():
                    print("** no instance found **")
                elif idx in all_instance.keys():
                    del(all_instance[idx])
                    storage.save()

    def do_show(self, line):
        "print the string repr of an instance"
        if line == '':
            print('** class name missing **')
        else:
            lines = line.split(' ')
            if len(lines) > 0 and lines[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(lines) == 1:
                print("** instance id missing **")
            elif len(lines) > 1 and lines[0] in CLASSES:
                all_instance = storage.all()
                idx = "{0}.{1}".format(lines[0],lines[1])
                if idx not in all_instance.keys():
                    print("** no instance found **")
                elif idx in all_instance.keys():
                    print(all_instance[idx])

    def do_all(self, line):
        "Print all string repr of instance"
        if line == '':
            print('** class name missing **')
        elif line not in CLASSES and line != '.':
            print("** class doesn't exist **")
        elif line in CLASSES or line == '.':
            all_instance = storage.all()
            hold = []
            for i, j in all_instance.items():
                hold.append(j.__str__())
            print(hold)

    def do_update(self, line):
        "update the instance attribute"
        if line == '':
            print('** class name missing **')
        else:
            lines = line.split(' ')
            if len(lines) > 0 and lines[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(lines) == 1:
                print("** instance id missing **")
            elif len(lines) == 2:
                print("** attribute name missing **")
            elif len(lines) == 3:
                print("** value missing **")
            elif len(lines) > 3 and lines[0] in CLASSES:
                all_instance = storage.all()
                idx = "{0}.{1}".format(lines[0],lines[1])
                if idx not in all_instance.keys():
                    print("** no instance found **")
                elif idx in all_instance.keys():
                    model = all_instance[idx]
                    if isinstance(lines[3], str):
                        model.__dict__[lines[2]] = str(lines[3].replace('"',''))
                    elif isinstance(lines[3], int):
                        model.__dict__[lines[2]] = int(lines[3])
                    elif isinstance(lines[3], float):
                        model.__dict__[lines[2]] = float(lines[3])
                    eval(lines[0])(**model.to_dict())
                    storage.save()

    def default(self, line):
        "method called when the command prefix"
        "is not recognized"
        print("unknown command (%s)", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
