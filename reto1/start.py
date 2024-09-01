import subprocess, time

def start_process(command):
    process = subprocess.Popen(command, shell=True)
    return process

def main():
    commands = [
        'python PServer.py',
        'python PClient.py',
    ]
    server_process = start_process(commands[0])
    time.sleep(5)
    client_process = start_process(commands[1])
    
    try:
        server_process.wait()
        client_process.wait()
    except KeyboardInterrupt:
        server_process.terminate()
        client_process.terminate()

if __name__ == '__main__':
    main()