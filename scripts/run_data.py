import os
import time
import subprocess

batch_size = 8

def main():
    with open(os.devnull, 'w') as fnull:
        p_server = subprocess.Popen(['python','PipeSwitch/kill_restart/kill_restart.py','resnet152'], stdout=fnull, stderr=fnull)
        time.sleep(30)

        scheduling_cycle = 5
        interval_count = 10
        p_client = subprocess.Popen(['python', 'PipeSwitch/client/throughput.py', str(scheduling_cycle), str(interval_count)], stderr=fnull)

        while True:
            try:
                p_client.wait(1)
                break
            except:
                print (time.time())
                sys.stdout.flush()
                continue
        p_server.kill()

if __name__ == '__main__':
    main()