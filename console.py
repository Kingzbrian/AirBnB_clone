#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter.
    """

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        """Quit command to exit the program.\n"""
        
        exit(0)

    def do_EOF(self, args):
        """Handles EOF to exit the program.\n"""
        
        exit(0)

if __name__ == '__main__':
    """
    Entry point for the loop.
    """
    HBNBCommand().cmdloop()
