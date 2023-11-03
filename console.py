#!/usr/bin/python3
""" command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class for a command-line program """
    prompt = "(hbnb) "
    list_class = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
        ]

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

    def do_create(self, arg):
        """Creates new instance of BaseModel and saves it to the JSON file."""
        if not arg:
            print("** class name missing **")
            return
        argx = arg.split()

        if argx[0] not in self.list_class:
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        storage.new(obj)
        storage.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        argx = arg.split()
        if not argx:
            print("** class name missing **")
            return

        if argx[0] not in self.list_class:
            print("** class doesn't exist **")
            return
        if len(argx) > 1:
            obj_dict = storage.all()
            key = "{}.{}".format(argx[0], argx[1])
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        argx = arg.split()
        if not argx:
            print("** class name missing **")
            return
        if argx[0] not in self.list_class:
            print("** class doesn't exist **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(argx[0], argx[1])
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances.
        """
        argx = arg.split()
        obj_dict = storage.all()
        obj_list = []
        if not argx:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            if argx[0] not in self.list_class:
                print("** class doesn't exist **")
                return
            for key, obj in obj_dict.items():
                if argx[0] == obj.__class__.__name__:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        argx = arg.split()
        obj_dict = storage.all()
        class_name = argx[0]

        if not argx:
            print("** class name missing **")
            return
        obj_id = argx[1]
        if class_name not in self.list_class:
            print("** class doesn't exist **")
            return
        if len(argx) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in obj_dict:
            print("** no instance found **")
            return
        if len(argx) < 3:
            print("** attribute name missing **")
            return
        if len(argx) < 4:
            print("** value missing **")
            return
        attribute_name = argx[2]
        attribute_value = argx[3]
        obj = obj_dict[obj_key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
