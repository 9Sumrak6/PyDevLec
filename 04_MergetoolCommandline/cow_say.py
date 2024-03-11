import shlex
import cmd

import readline
import rlcompleter

from cowsay import cowsay, list_cows, make_bubble, cowthink, Option

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

class Cow_cmd(cmd.Cmd):
    prompt = ':->'

    cowsay_params = ['-e', '-T', '-f']

    tongues = ['U ', ' U']
    eyes = ['==', 'XX', '$$', '@@', '**', '--', 'OO', '..']


    def do_cowsay(self, args):
        """
        Similar to the cowsay command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting
        cowsay string

        :param message: The message to be displayed
        :param cow: -f – the available cows can be found by calling list_cows
        :param eyes: -e or eye_string
        :param tongue: -T or tongue_string

        Correct example: cowsay I love MSU -e ^^ -T U
        Incorrect example: cowsay -e ^^ -T U (there is no message)
        """
        s_args = shlex.split(args, 0, 0)

        if len(args) == 0:
            print("Invalid arguments. Print 'help' to know args")
        else:
            tongue = Option.tongue
            eyes = Option.eyes
            cow = 'default'
            message = ''

            i, fl = 0, 1
            while i < len(s_args):
                if s_args[i] == '-e':
                    fl = 0
                    eyes = s_args[i+1]
                elif s_args[i] == '-T':
                    fl = 0
                    tongue = s_args[i+1]
                elif s_args[i] == '-f':
                    fl = 0
                    cow = s_args[i+1]
                elif fl == 1:
                    if message != '':
                        message += ' '

                    message += s_args[i]
                    i -= 1
                else:
                    print("Invalid params")
                    return 1

                i += 2
            if message == '':
                print("Invalid arguments. Print 'help' to know args")
            else:
                print(cowsay(message, cow=cow, eyes=eyes, tongue=tongue))


    def complete_cowsay(self, text, line, begidx, endidx):
        res = shlex.split(line[:begidx], 0, 0)

        if res[-1] == '-e':
            return [c for c in self.eyes if c.startswith(text)]
        elif res[-1] == '-f':
            return [c for c in list_cows() if c.startswith(text)]
        elif res[-1] == '-T':
            return [c for c in self.tongues if c.startswith(text)]


    def do_list_cows(self, args):
        """
        Lists all cow file names in the given directory
        """
        print(*list_cows())


    def do_make_bubble(self, args):
        """
        Wraps text is wrap_text is true, then pads text and sets inside a bubble.
        This is the text that appears above the cows
        """
        print(make_bubble(args))


    def do_cowthink(self, args):
        """
        Similar to the cowthink command. Parameters are listed with their
        corresponding options in the cowthink command. Returns the resulting
        cowthink string

        :param message: The message to be displayed
        :param cow: -f – the available cows can be found by calling list_cows
        :param eyes: -e or eye_string
        :param tongue: -T or tongue_string

        Correct example: cowsay I love MSU -e ^^ -T U
        Incorrect example: cowsay -e ^^ -T U (there is no message)
        """
        s_args = shlex.split(args, 0, 0)

        if len(args) == 0:
            print("Invalid arguments. Print 'help' to know args")
        else:
            tongue = Option.tongue
            eyes = Option.eyes
            cow = 'default'
            message = ''

            i, fl = 0, 1
            while i < len(s_args):
                if s_args[i] == '-e':
                    fl = 0
                    eyes = s_args[i+1]
                elif s_args[i] == '-T':
                    fl = 0
                    tongue = s_args[i+1]
                elif s_args[i] == '-f':
                    fl = 0
                    cow = s_args[i+1]
                elif fl == 1:
                    if message != '':
                        message += ' '

                    message += s_args[i]
                    i -= 1
                else:
                    print("Invalid params")
                    return 1

                i += 2
            if message == '':
                print("Invalid arguments. Print 'help' to know args")
            else:
                print(cowthink(message, cow=cow, eyes=eyes, tongue=tongue))


    def complete_cowthink(self, text, line, begidx, endidx):
        res = shlex.split(line[:begidx], 0, 0)

        if res[-1] == '-e':
            return [c for c in self.eyes if c.startswith(text)]
        elif res[-1] == '-f':
            return [c for c in list_cows() if c.startswith(text)]
        elif res[-1] == '-T':
            return [c for c in self.tongues if c.startswith(text)]


    def do_EOF(self, args):
        """
        Needs to end the input
        """
        return True


if __name__ == '__main__':
    Cow_cmd().cmdloop()
