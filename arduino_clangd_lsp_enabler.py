import subprocess
import os

class Src:
    def __init__(self, name="", pwd="", args=[]):
        self.args = args.copy()
        self.args.append(name)
        self.name = name
        split = name.split("/")
        self.out = name.split(".")[0] + ".o"
        self.dir = os.path.join(pwd, *split[:-1])

class   Data:
    def __init__(self, target="compile_commands.json"):
        self.target = target
        self.pwd = os.getcwd()
        self.args = []
        self.args.append("-DLSP")
        # todo: this is specific for the board im testing with
        # idk how do find this out without looking at the pysical chip atm
        # (for my cheap aliexprss boards)
        self.args.append("-D__AVR_ATmega328P__")
        self.args.append("usr/bin/cc")
        # not needed anymore I think
        #self.args = self.args + self.run_make_command("echo_includes")
        self.args = self.args + self.find_arduino_headers()
        sources = self.run_make_command("echo_sources")
        self.sources = [Src(src, self.pwd, self.args) for src in sources]

    def run_make_command(self, target):
        try:
            sub_data = subprocess.run(["make", target], capture_output=True,
                                      text=True)
            return sub_data.stdout.split()
        except subprocess.CalledProcessError as e:
            print(f"error: make {target}: {e}")
            return []

    def make_ultimate_arduino_header_for_lsp(self):
        head = ' echo "#ifdef LSP > lsp.h" '
        find = " find ~ -wholename *arduino*'.h' -type f -exec basename {} ; "
        loop = ' while read line ; '
        includes = ' do echo "#include <${line}>;" ; done >> lsp.h '
        tail = ' echo  #endif >> lsp.h '
        command = head + ' && ' + find + ' | ' + loop + ' && ' + tail
        try:
            sub = subprocess.run(command.split())
        except subprocess.CalledProcessError as e:
            print(f'{command}: Error: {e}')

    def find_arduino_headers(self):
        try:
            sub = subprocess.run(
                ["find", os.path.expanduser("~"), "-type", "f", "-wholename",
                 "*arduino*.h", "-exec", "grep", "-Iq", ".","{}", ";",
                 "-print"],
                capture_output=True,
                text=True
            )
            header_paths = sub.stdout.split()
            include_dirs = {os.path.dirname(path) for path in header_paths}
            return [f"-I{dir}" for dir in include_dirs]
        except sub.CalledProcessError as e:
            print(f"error: find: {e}")
            return []

    def write_src_entry(self, src, file):
        args_formatted = "[\n    " + ",\n    ".join(f'"{arg}"' for arg in src.args) + "\n]"
        entry = f"""
    {{
        "arguments": {args_formatted},
        "directory": "{src.dir}",
        "file": "{src.name}",
        "output": "{src.out}"
    }}"""
        file.write(entry)

    def generate(self):
        with open(self.target, "w") as file:
            file.write("[")
            for src in self.sources:
                first = True
                for src in self.sources:
                    if not first:
                        file.write(",")
                    first = False
                    self.write_src_entry(src, file)
                file.write("\n]")

#class UltimateArduinoHeader():
#    def generate(self):
#        find = subprocess.run(['find', '/home', '-type', 'f', '-wholename', "*arduino*'.h'"],
#                capture_output=True, text=True)
#        find.wait()
#        with open("lsp.h", "w") as header:
#            header.write('#ifdef LSP\n')
#            for header in find.stdout:
#                header.write(f"#include <{line.split('/')[-1]}>\n")
#            header.write('#endif')

def ultimate_arduino_header():
    command = "echo '#ifdef LSP' > lsp.h && find ~ -wholename *arduino*'.h' -type f -exec basename {} \; | while read line; do echo \"#include <${line}>;\"; done >> lsp.h && echo '#endif' >> lsp.h"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f'building ultimater failed(\n{command}\nfailed: {e}')

if __name__ == "__main__":
    #header = UltimateArduinoHeader()
    #header.generate()
    ultimate_arduino_header()
    data = Data()
    data.generate()


