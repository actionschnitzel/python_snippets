import subprocess

def get_wm():

    output = subprocess.run(['wmctrl', '-m'], text=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if output.stderr:
        return(output.stderr)
    else:
        return(output.stdout)

print(get_wm())