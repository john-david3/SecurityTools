"""Program to brute force a password by checking the p67assword against a list of the top 100k passwords and then trying every combination
    up to a certain length of characters"""

import pyautogui, string, time

def common_check(pwd, filename):
    """Check all the top 100k most common passwords"""
    p_file = open(filename, "r", encoding="utf-8")
    common_pwds = p_file.readlines()
    for word in common_pwds:
        word = word.strip()
        if word == pwd:
            print("Password is: ", word)
            p_file.close()
            return True

    p_file.close()
    return False

def generate_combos(charset, pwd, max_length):
    """Generate all combinations of characters up until a max character limit"""
    for length in range(1, max_length + 1):
        backtrack(charset, length, "", pwd)

def backtrack(charset, length, test_pwd, pwd):
    """Back track on the passwords to attempt every combination of password. Work with generate_combos function"""
    if test_pwd == pwd:
        print(f"Password Found: {test_pwd} ")
        end_time = time.time()
        time_taken = end_time - start_time
        print("Time taken to find password:", time_taken)
        exit()

    if length == 0:
        print(f"<=== {test_pwd} ===>")
        return
    
    for char in charset:
        new_pwd = test_pwd + char
        backtrack(charset, length - 1, new_pwd, pwd)

#Check if the password has been found
pass_found = False

#List of printable characters
charset = string.printable[:94]
all_chars = list(charset)

#User entered password
pwd = pyautogui.password("Enter a password:")

start_time = time.time()
pass_found = common_check(pwd, "10-million-password-list-top-1000000.txt")

#If password not in top 100k passwords
if not pass_found:
    generate_combos(all_chars, pwd, 16)

end_time = time.time()
time_taken = end_time - start_time
print("Time taken to find password:", time_taken)
