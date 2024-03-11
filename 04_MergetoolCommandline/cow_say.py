import shlex
import cmd
from cowsay import cowsay, list_cows, make_bubble, cowthink, Option


class Cow_cmd(cmd.Cmd):
    cowsay_params = ['-e', 'eye_string', '-T', 'toungue_string', '-f']
    def do_cowsay(self, args):
        s_args = shlex.split(args)

        if len(args) == 0:
            print("Invalid arguments")
        elif len(args) == 1:
            cowsay(s_args[0])
        else:

    def do_list_cows(self, args):
        print(2)

    def do_make_bubble(self, args):
        print(3)

    def do_cowthink(self, args):
        print(4)


if __name__ == '__main__':
    Cow_cmd().cmdloop()

