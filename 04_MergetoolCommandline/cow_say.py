import shlex
import cmd
from cowsay import cowsay, list_cows, make_bubble, cowthink, Option

class Cow_cmd(cmd.Cmd):
    cowsay_params = ['-e', '-T', '-f']

    def do_cowsay(self, args):
        s_args = shlex.split(args)

        if len(args) == 0:
            print("Invalid arguments")
        else:
            tongue = Option.tongue
            eyes = Option.eyes
            cow = 'default'

            i = 1
            while i < len(s_args):
                if s_args[i] not in self.cowsay_params:
                    print("Invalid params")
                    return 1
                if s_args[i] == '-e':
                    eyes = s_args[i+1]
                elif s_args[i] == '-T':
                    tongue = s_args[i+1]
                else:
                    cow = s_args[i+1]
                i += 2
            print(tongue, eyes, cow)
            print(cowsay(s_args[0], cow=cow, eyes=eyes, tongue=tongue))

    def do_list_cows(self, args):
        print(cowsay.list_cows())

    def do_make_bubble(self, args):
        print(3)

    def do_cowthink(self, args):
        print(4)


if __name__ == '__main__':
    Cow_cmd().cmdloop()

