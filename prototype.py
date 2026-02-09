import socket, argparse, errno

total_ports_scanned = 0
total_ports_open = 0
total_ports_closed = 0
total_ports_unknown = 0

def output(code, port):
    global total_ports_scanned, total_ports_open, total_ports_closed, total_ports_unknown
    total_ports_scanned += 1
    if code == 0:
        total_ports_open += 1
        print(f"Port {port} is OPEN")
    elif code == errno.ECONNREFUSED:
        print(errno.ECONNREFUSED)
        total_ports_closed += 1
        print(f"Port {port} is CLOSED")
    else:
        total_ports_unknown += 1
        print(f"Port {port} is UNKNOWN")

def scan_range(target, port_start, port_end):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    print(f"\nScanning Ports {port_start} to {port_end}...")
    for port in range(port_start, port_end + 1):
        scan(target, port)

def scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    print(f"\nScanning port {port}...")

    res = sock.connect_ex((target, port))

    sock.close()

    output(res, port)
   

def main():
    parser = argparse.ArgumentParser(description="Port Scanner - MVP")
    parser.add_argument("target", help="IP or hostname to scan")
    parser.add_argument("-p", "-pr", "--port", "--portrange", default=80, help="Port(s) to scan")

    args = parser.parse_args()

    print("========== WELCOME TO ESTROLABS PORT SCANNER - MVP ==========")

    consent = input("Are you sure that you have permission to scan this target or that the target is correct? (YES / NO)\n> ")

    if consent.lower() != "yes":
        print("Please ensure you have permission to scan this target and then try again later!")
        return

    if '-' in args.port:
        scan_range(args.target, int(args.port.split("-")[0]), int(args.port.split("-")[1])) 
    else:
        scan(args.target, int(args.port))

    print("\n========= Port Scanning Stats =========")
    print(f"\nTotal Ports Scanned: {total_ports_scanned}")
    print(f"Total Ports Open:      {total_ports_open}")
    print(f"Total Ports Closed:    {total_ports_closed}")
    print(f"Total Ports Unknown:   {total_ports_unknown}\n")

if __name__ == "__main__":
    main()