#!/usr/bin/python3
""" command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class for a command-line program """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Quit the command interpreter when EOF is encountered.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line (just pressing ENTER).
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
