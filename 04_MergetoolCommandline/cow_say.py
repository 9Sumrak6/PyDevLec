import shlex
import cmd
from cowsay import cowsay, list_cows, make_bubble, cowthink, Option


class Cow_cmd(cmd.Cmd):
    def do_cowsay(self, args):
        print(1)

    def do_list_cows(self, args):
        print(2)

    def do_make_bubble(self, args):
        print(3)

    def do_cowthink(self, args):
        print(4)


if __name__ == '__main__':
    Cow_cmd().cmdloop()
