import global_variables
import threading
import paramiko
import interactive


class Ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, address, username):
        print("Connecting to server", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username)

        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def close_connection(self):
        if self.client is not None:
            self.client.close()
            self.transport.close()

    def open_shell(self):
        self.shell = self.client.invoke_shell()

    def send_shell(self, command):
        if self.shell:
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")

    def process(self):
        global connection
        while True:
            # Print data when available
            if self.shell is not None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)
                strdata = str(alldata, "utf8")
                strdata.replace('\r', '')
                print(strdata, end="")
                if strdata.endswith("$ "):
                    print("\n$ ", end="")


def new_connection(server):
    connect = Ssh(server, global_variables.user)
    connect.open_shell()
    interactive.start_interactive()
