import socket
import time 

host_up = {0, 111}

def up(host, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        start = time.time()
        result = s.connect_ex((host, 80))
        if result in host_up:
            return True
        else:
            return False
        s.close()
    except Exception as e:
        print(e)


def scan(host, timeout, ports):
    host_status = up(host, timeout)
    
    open_ports = {
            
        }

    if not host_status:
        print("Host is down.")
    else:
        try:
            for p in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)

                result = s.connect_ex((host, p))
                if result == 0:
                    try:
                        banner = s.recv(1024).decode().strip()
                    except Exception:
                        banner = "unknown"
                    open_ports.update({p: banner})
                s.close()
            print("HOST       SERVICE")
            for key, value in open_ports.items():
                print("{:<{kw}} {}".format(key, value, kw=10))
        except Exception as e:
                print(e)
