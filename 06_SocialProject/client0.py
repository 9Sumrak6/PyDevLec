import cmd
import sys
#import threading
#import time
#import readline
import socket


class simple(cmd.Cmd):
    
    def __init__(self, sock):
        super().__init__()

        self.sock = sock

    def do_login(self, arg): 
        self.sock.sendall(f"login {arg}\n".encode())
        data = self.sock.recv(1024).decode()        
        print(data)

    def do_who(self, arg):
        self.sock.sendall(f"who\n".encode())
        data = self.sock.recv(1024).decode()
        print(data)

    def do_cows(self, arg):
        self.sock.sendall(f"cows\n".encode())
        data = self.sock.recv(1024).decode()
        print(data)

    def do_say(self, arg):
        args = arg.split()
        self.sock.sendall(f"say {args[0]} {" ".join(args[1:])}\n".encode())
        data = self.sock.recv(1024).decode()
        print(data) 

    def do_yield(self, arg):
        self.sock.sendall(f"yield {arg}\n".encode())
        data = self.sock.recv(1024).decode()
        print(data) 

    def do_quit(self, arg):
        print(arg)

    def complete_attack(self, text, line, begidx, endidx):
        self.sock.sendall(f"yield {arg}\n".encode())
        data = self.sock.recv(1024).decode()

    def complete_say(self, text, line, begidx, endidx):

    def do_EOF(self, args):
        return True

'''
def spam(cmdline, timeout, count):
    for i in range(count):
        time.sleep(timeout)
        print(f"\nI'm a message № {i}!\n{cmdline.prompt}{readline.get_line_buffer()}", end="", flush=True)
'''

if __name__ == "__main__":
    host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
    port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        cmdline = simple(s)
        # timer = threading.Thread(target=spam, args=(cmdline, 3, 10))
        # timer.start()
        cmdline.cmdloop()
