#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_create(self, arg):
        if arg:
            instance = arg()
            return instance.id
        else:
            print("** class name missing **")
    def do_EOF(self, arg):
        """exits the program"""
        return True
    def do_quit(self, arg):
        """exits the program"""
        return True
    def emptyline(self):
        """An empty line"""
        if self.lastcmd:
            return self.onecmd(self.lastcmd)
if __name__ == '__main__':
            HBNBCommand().cmdloop()
