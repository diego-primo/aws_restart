import os
import subprocess


os.system("ls")
print('\n')
subprocess.run(["ls"])
#subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

print('\n')
subprocess.run(["ls","-l"])

print('\n')
subprocess.run(["ls","-l","README.md"])

print('\n')
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print('\n')
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])