with open('/etc/os-release') as f:
    if 'NAME="Linux Mint"' in f.read():
        print("true")
        
    else:
        print("false")