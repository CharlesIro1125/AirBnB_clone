#!/usr/bin/python3
"The console entry point"
import cmd
from models import storage
from models.base_model import BaseModel
import signal


class HBNBCommand(cmd.Cmd):
    "A command line interface"

    prompt = '(hbnb)'
    intro = 'Cmd interpreter'
    _interrupted = False

    def __init__(self):
        signal.signal(signal.SIGINT, handler=self._ctrl_c_handler)
        super().__init__()

    def _ctrl_c_handler(self, signal, frame):
        print('')
        exit(0)

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

    def do_EOF(self, line):
        "The EOF method returns true"
        if line:
            print("args passed")
        else:
            print("Exit")
            return True

    def do_create(self, line):
        "creates an instance of BaseModel"
        if line == 'BaseModel':
            new_model = BaseModel()
            new_model.name = 'My_First_Model'
            new_model.my_number = 89
            new_model.save()
            print(new_model.id)
        elif line == '':
            print('** class name missing **')
        elif line != 'Basemodel':
            print("** class doesn't exist **")

    def do_exit(self, line):
        return True

    def do_quit(self, line):
        "The quit method returns True"
        if line:
            print("args passed(quit)")
        else:
            print("quit")
            return True

    def emptyline(self):
        "method called when an empty line is entered"
        "to the prompt"
        print("emptyline")
        return cmd.Cmd.emptyline(self)

    def do_show(self, line):
        "print the string repr of an instance"
        if line == '':
            print('** class name missing **')
        else:
            lines = line.split(' ')
            if len(lines) > 0 and lines[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(lines) == 1:
                print("** instance id missing **")
            elif len(lines) > 1 and lines[0] == 'BaseModel':
                all_instance = storage.all()
                hold = []
                for key in all_instance.keys():
                    hold.append(key.split('.')[1])
                if lines[1] not in hold:
                    print("** no instance found **")
                elif lines[1] in hold:
                    idx = hold.index(lines[1])
                    print(all_instance.values()[idx])

    def default(self, line):
        "method called when the command prefix"
        "is not recognized"
        print("unknown command (%s)", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
