#!/usr/bin/python3
""" command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                obj_dict = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in obj_dict:
                    print(obj_dict[key])
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                obj_dict = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in obj_dict:
                    del obj_dict[key]
                    storage.save()
                else:
                    print("** no instance found **")
            except Exception as e:
                print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representations of all instances.
        """
        args = line.split()
        obj_dict = storage.all()
        obj_list = []
        if not args:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            try:
                for key, obj in obj_dict.items():
                    if args[0] == obj.__class__.__name__:
                        obj_list.append(str(obj))
                if not obj_list:
                    print("** class doesn't exist **")
                    return
            except Exception as e:
                print("** class doesn't exist **")

        print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        """
        args = line.split()
        obj_dict = storage.all()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            obj_id = args[1]

            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_key = "{}.{}".format(class_name, obj_id)
            if obj_key not in obj_dict:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            if len(args) < 4:
                print("** value missing **")
                return

            attribute_name = args[2]
            attribute_value = args[3]

            obj = obj_dict[obj_key]
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        except Exception as e:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
