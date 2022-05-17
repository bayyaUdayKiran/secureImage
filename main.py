import subprocess as sb

print("***MENU***")
print("""
    A. ENCRYPT
    B. DECRYPT
    C. EXIT
""")

choice = input("Your choice: ")
if ((choice == 'A')or(choice == 'a')):
    process = sb.run("python3 encrypt.py", capture_output=True, shell=True)
    std_out = process.stdout.decode('UTF-8')
    std_err = process.stderr.decode('UTF-8')
    if std_err == '':
        print(std_out)
    else:
        print(std_err)



elif ((choice == 'B')or(choice == 'b')):
    process = sb.run("python3 decrypt.py", capture_output=True, shell=True)
    std_out = process.stdout.decode('UTF-8')
    std_err = process.stderr.decode('UTF-8')
    if std_err == '':
        print(std_out)
    else:
        print(std_err)

    


