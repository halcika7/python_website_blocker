import tkinter as tk

class Blocker:
    def __init__(self):
        sites_to_block = ['www.facebook.com', 'facebook.com']
        self.hosts_path = '/etc/hosts'
        # r"C:\Windows\System32\drivers\etc\hosts" ---- for Windows
        self.redirect = "127.0.0.1"
        self.blocked = False

        self.root = tk.Tk()
        self.root.title("Block websites")
        self.root.geometry("450x200")  # set window

        self.label = tk.Label(
            self.root, text="Enter websites to block in format ***www.facebook.com,facebook.com")
        self.label.grid()

        # Entry Box
        self.value = tk.StringVar(value=",".join(sites_to_block))
        self.entryValue = tk.Entry(self.root, width=50, textvariable=self.value)
        self.entryValue.grid()

        self.button = tk.Button(self.root, text="Block Websites", command=self.block)
        self.button.grid()

    def start(self):
        self.root.mainloop()

    def block(self):
        
        if not self.blocked:
            with open(self.hosts_path, 'r+') as hostfile:
                hosts_content = hostfile.read()
                for site in self.entryValue.get().split(','):
                    if site not in hosts_content:
                        hostfile.write(self.redirect + ' ' + site + '\n')
            self.button.config(text="Unblock Websites")
            self.blocked = True
            self.entryValue.config(state=tk.DISABLED)

        else:
            with open(self.hosts_path, 'r+') as hostfile:
                lines = hostfile.readlines()
                hostfile.seek(0)
                for line in lines:
                    if not any(site in line for site in self.entryValue.get().split(',')):
                        hostfile.write(line)
                hostfile.truncate()
            
            self.button.config(text="Block Websites")
            self.blocked = False
            self.entryValue.config(state=tk.NORMAL)


# sudo python main.py
if __name__ == '__main__':
    block = Blocker()
    block.start()
