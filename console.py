#!/usr/bin/python3
'''
    Represents a  FileStorage class
'''
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
        HBNB Command interpreter
    '''
    prompt = "(hbnb) "
    classes = [
        "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
    all_objects = models.storage.all()

    def do_create(self, line):
        'Create  command to create a new instance of a class\n'
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.classes:
            '''
            eval(args): execute the python expression
            eval(args)(self):return the object equivalent
            to the python expression'''
            new_object = eval(args[0])(self)
            #print ((eval(args[0])()))
            new_object.save()
            print(new_object.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        'Show command to prints the string representation of an instanced\n'
        args = shlex.split(line)
        '''args = self.argparser.parse_args(line.split(line))'''
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in HBNBCommand.all_objects.keys():
                print("** no instance found **")
        else:
            print(HBNBCommand.all_objects[args[0] + "." + args[1]])

    def do_destroy(self, line):
        'Deletes an instance based on the class name and id\n'
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in HBNBCommand.all_objects.keys():
            print("** no instance found **")
        else:
            del HBNBCommand.all_objects[args[0] + "." + args[1]]
            '''{key :obj} = clase.id'''
            models.storage.save()

    def do_all(self, line):
        'Prints all string representation of all instancesq\n'
        args = shlex.split(line)
        if len(args) == 0:
            list1 = []
            for key, value in HBNBCommand.all_objects.items():
                list1.append(value.__str__())
            print(list1)
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            list1 = []
            for key, value in HBNBCommand.all_objects.items():
                if type(value) == eval(args[0]):
                    list1.append(value.__str__())
            print(list1)

    def do_update(self, line):
        'Updates an instance- attribute based on the class name and id\n'
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in HBNBCommand.all_objects.keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            dic2 = HBNBCommand.all_objects[key]  # all_objects = storage.all()
            args[2]  # name attribute
            args[3] = args[3].replace("\"", "")  # args[3] = value attribute
            setattr(dic2, args[2], args[3])
            dic2.save()

    def do_EOF(self, line):
        'EOF command to exit the program\n'
        return True

    def do_quit(self, args):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        'do anything\n'
        pass

    def default(self, line):
        'Called on an input line when the command prefix is not recognized'
        line_copy = line.replace("\"", "").replace("(", ".").replace(
            ")", ".").replace(",", "")
        args = line_copy.split(".")
        if len(args) > 1:
            if args[1] == "all":
                self.do_all(args[0])
            elif args[1] == "count":
                self.do_count(args[0])
            elif args[1] == "show":
                self.do_show(args[0] + " " + args[2])
            elif args[1] == "destroy":
                self.do_destroy(args[0] + " " + args[2])
            elif args[1] == "update":
                self.do_update(args[0] + " " + args[2])
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, line):
        'Count command retrieve the number of instances of a class:'
        args = shlex.split(line)
        if len(args) == 0:
            list1 = []
            for key, value in HBNBCommand.all_objects.items():
                list1.append(value.__str__())
            print(len(list1))
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            list1 = []
            for key, value in HBNBCommand.all_objects.items():
                if type(value) == eval(args[0]):
                    list1.append(value.__str__())
            print(len(list1))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
