import shlex
import cmd
import readline
import rlcompleter
from cowsay import cowsay, list_cows, make_bubble, cowthink, Option

class Cow_cmd(cmd.Cmd):
    prompt = ':->'

    cowsay_params = ['-e', '-T', '-f']

    tongues = ['U ', ' U']
    eyes = ['==', 'XX', '$$', '@@', '**', '--', 'OO', '..']


    def do_cowsay(self, args):
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


    def do_list_cows(self, args):
        print(*list_cows())


    def do_make_bubble(self, args):
        print(make_bubble(args))


    def do_cowthink(self, args):
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


    def do_EOF(self, args):
        return True


if __name__ == '__main__':
    Cow_cmd().cmdloop()
