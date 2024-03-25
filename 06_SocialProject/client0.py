import cmd
import sys
import multiprocessing
import time
import readline
import socket
import shlex


prompt = ":->"

class simple(cmd.Cmd):
    
    prompt = prompt

    def __init__(self, sock, catcher):
        super().__init__()

        self.sock = sock
        self.catcher = catcher

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
#        data = self.sock.recv(1024).decode()
#        print(data) 

    def do_yield(self, arg):
        self.sock.sendall(f"yield {arg}\n".encode())
#        data = self.sock.recv(1024).decode()
#        print(data) 

    def do_quit(self, arg):
        self.sock.sendall(f"quit\n".encode())
        
        self.catcher.terminate()
        self.catcher.join()
        

        return True

    def complete_login(self, text, line, begidx, endidx):
        self.sock.sendall('cows\n'.encode())
        data = self.sock.recv(1024).decode().replace('{', '').replace('}', '').replace("'", "").replace(",", "").split()[2:]

        return [c for c in data if c.startswith(text)]

    def complete_say(self, text, line, begidx, endidx):
        self.sock.sendall('who\n'.encode())
        data = self.sock.recv(1024).decode().replace('{', '').replace('}', '').replace("'", "").replace(",", "").split()[2:]

        return [c for c in data if c.startswith(text)]
    
    def do_EOF(self, args):
        return True


def spam(conn):
    while True:
        print('\n' + conn.recv(1024).decode() + prompt, end='')
        time.sleep(1)

if __name__ == "__main__":
    host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
    port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        catcher = multiprocessing.Process(target=spam, args=[s])
        catcher.start()

        cmdline = simple(s, catcher)
        cmdline.cmdloop()
