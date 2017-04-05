#!/usr/bin/python2
import commands
import time
while True:
    try:
        output = commands.getstatusoutput('nvidia-smi')
        output = output[1].split('\n')
        flag1 = False
        flag2 = False
        for line in output:
            if 'Processes:' in line:
                flag1 = True
                print(line)
                continue
            if flag1 and '='*30 in line:
                flag2 = True
                print(line)
                continue
            if flag2:
                if 'No running processes found' in line or '-'*30 in line:
                    flag2 = False
                    print(line)
                    continue
                pid = line.split()[2]
                results = commands.getstatusoutput('ps aux|grep '+pid)[1].split('\n')
                for res in results:
                    if res.split()[1]==pid:
                        name = res.split()[0]
                        line = line.replace(' '*(8-len(pid))+pid, ' '*(8-len(name))+name)
            print(line)
        time.sleep(2)
    except KeyboardInterrupt:
        break
