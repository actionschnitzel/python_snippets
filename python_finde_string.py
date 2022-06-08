with open("/boot/config.txt") as pi_conf:
    datafile = pi_conf.readlines()
for line1 in datafile:
    if 'gpu_freq' in line1:
        print(line1[9:])
