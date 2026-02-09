###### MODULES ######
import socket, argparse, errno

total_ports_closed_count = 0
total_ports_unknown_count = 0
total_ports_open_count = 0

def scan_port(target, port, timeout):
    global total_ports_closed_count
    global total_ports_unknown_count
    global total_ports_open_count

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    print(f"Scanning Port {port}...")
    res = sock.connect_ex((target, int(port)))
    sock.close()

    if res == 0:
        total_ports_open_count += 1
        print(f"{target}:{port} is OPEN\n")
    elif res == errno.ECONNREFUSED:
        total_ports_closed_count += 1
        print(f"{target}:{port} is CLOSED\n")    
    else:
        total_ports_unknown_count += 1
        print(f"{target}:{port} is UNKNOWN\n")    

###### ENTRY POINT ######
def main():
    global total_ports_closed_count
    global total_ports_unknown_count
    global total_ports_open_count

    total_ports_scanned_count = 0

    print("========== ESTROLABS Port Scanner V(MVP) - 2026 ==========")
    arg_parser = argparse.ArgumentParser(description="ESTROLABS Port Scanner V(MVP) - 2026")
    arg_parser.add_argument("-t", "--target", help="IP or Domain Name / Host Name to scan")
    arg_parser.add_argument("-p", "--port", "--ports", default=8000, help="Port(s) to scan")
    arg_parser.add_argument("-i", "--timeout", default=3, help="Number of seconds to wait for a target to respond")
    args = arg_parser.parse_args()
    consent = input("Please ensure you have permission to scan this target and or the target is correctly inputed! (YES/NO)?\n> ")
    if consent.lower() != "yes":
        print("Sorry you did not verify consent therefore try again later!")
        exit()
        quit()
    
    print("")

    port_type = "s"
    if "-" in args.port:
        port_type = "r"
    elif "," in args.port:
        port_type = "m"
    port_multiple = []
    port_range_start = 0
    port_range_end = 0
    if port_type == "m":
        for port in args.port.split(","):
            port_multiple.append(port)
    elif port_type == "r":
        port_range_start = args.port.split("-")[0]
        port_range_end = args.port.split("-")[1]

    if port_type == "s":
        total_ports_scanned_count += 1
        scan_port(args.target, args.port, args.timeout)
    
    if port_type == "m":
        for port in port_multiple:
            total_ports_scanned_count += 1
            scan_port(args.target, port, args.timeout)

    if port_type == "r":
        for port in range(int(port_range_start), int(port_range_end) + 1):
            total_ports_scanned_count += 1
            scan_port(args.target, port, args.timeout)
    
    print("---------- Port Scan COMPLETE - Stats ----------")
    print(f"Total Ports Scanned: {total_ports_scanned_count}")
    print(f"Total Ports Open: {total_ports_open_count}")
    print(f"Total Ports Closed: {total_ports_closed_count}")
    print(f"Total Ports Unknown: {total_ports_unknown_count}")

    
if __name__ == "__main__":
    main()