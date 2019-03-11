import subprocess
from datetime import datetime
class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
    def __call__(self): return self.impl()
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
getch=_Getch()

Vars=input('Enter the variables (i.e.,1234):')
Count=input('Enter the number (i.e.,100):')
Count=int(Count)

Var_count={}
Mistakes=[]

for v in Vars:
    Var_count[v]=0

Stop=input('Press Enter to start. Print q to quit the program.')
stop=0

for c in range(Count):
    if stop==0:
        entry=getch()
        if entry!='q':
            if entry in Var_count:
                Var_count[entry]+=1
            else:
                Mistakes.append(entry)
        else:
            stop=1

if stop==0:
    try:
        command=['mplay32','/play','/close','sound.wav']
        cmd=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    except:
        try:
            command=['wmplayer','/play','/close','sound.wav']
            cmd=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
        except:
            try:
                command=['vlc','--play-and-exit','--quiet','sound.wav']
                cmd=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            except:
                print ('No audio player')

Sum=0
for vv in Var_count:
    Sum+=Var_count[vv]

Results=''
Results2='Percentage: '
for vvv in Var_count:
    Results=Results+vvv+': '+str(Var_count[vvv])+', '
    Results2=Results2+vvv+' '+(str(Var_count[vvv]/float(Sum)*100))[0:4]+'%, '

print ('---')
print ('Raw results:', Results[0:len(Results)-2])
print ('Counted cells:',str(Sum))
print (Results2[0:len(Results2)-2])
if Mistakes!=[]:
    report=''
    for m in Mistakes:
        report+=m
        report+=', '
    print ('Typing mistakes:', report[0:len(report)-2])
now=datetime.now()
time=str(now.hour)+':'+str(now.minute)
date=str(now.day)+'/'+str(now.month)+'/'+str(now.year)
print (time,date)
print ('---')
print ('---')