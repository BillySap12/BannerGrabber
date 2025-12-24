import socket
import time

host_up = {0, 111}

def sn(host, timeout, ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        start = time.time()
        result = s.connect_ex((host, 80))
        if result in host_up:
            end = time.time()
            elapsed_time = end - start
            print(f"\nScan report for {host}")
            print(f"{host} is up ({elapsed_time:.6f}s)")
        else:
            end = time.time()
            elapsed_time = end - start
            print(f"\nScan report for {host}")
            print(f"{host} is down ({elapsed_time:.6f}s)")
            print(f"BannerGrabber complete: 1 host scanned in {elapsed_time:.6f}s")
        s.close()
    except Exception as e:
        print(e)
