###### MODULES ######
# TODO: 1. MODULE: Import socket 
# TODO: 2. MODULE: Import argparse 
# TODO: 3. MODULE: Import errno 

def scan_port(target, port, timeout):
    # TODO: 13. LOGIC: Create socket
    # TODO: 14. LOGIC: Set socket timeout
    # TODO: 15 OUTPUT: Scanning Port {port}...
    # TODO: 16. LOGIC: Connect to target on port from socket
    # TODO: 17. LOGIC: Close Socket
    # TODO: 17. LOGIC: Return connection error/status code

    pass

###### ENTRY POINT ######
def main():

    # TODO: 3.1. LOGIC: Variable - Total Ports Scanned
    # TODO: 3.2. LOGIC: Variable - Total Ports Oppen
    # TODO: 3.3. LOGIC: Variable - Total Ports Closed
    # TODO: 3.4. LOGIC: Variable - Total Ports Unknown

    # TODO: 4. OUTPUT: Welcome Banner / Header Message
    # TODO: 5. INPUT: Initialise Arg Parser
    # TODO: 6. INPUT:  Add arg target ip/domain
    # TODO: 7. INPUT:  Add arg port(s) as -p / --port / --ports
    # TODO: 8. INPUT:  Add arg timeout as -t / --timeout
    # TODO: 9. INPUT: Get Consent Input
    # TODO: 10. LOGIC: Check consent is aquired
    # TODO: 11. LOGIC: Parse Ports from 50-100 / 80,443,22
    # TODO: 12. LOGIC: Check if signular or multiple ports will be scanned
    # TODO: 13. LOGIC: If signular call scan_port function 
    
    # TODO: 14. LOGIC: If multiple loop through each port 
    # TODO: 14.1. LOGIC: Add 1 to count of total ports scanned
    # TODO: 14.2. LOGIC: Call scan_port function
    
    # TODO: 15. LOGIC: Check if return code is 0
    # TODO: 15.1. LOGIC: Add 1 to the count of total opened ports
    # TODO: 15.2. OUTPUT: 127.0.0.1:80 is OPEN

    # TODO: 16. LOGIC: Check if return code is 1006
    # TODO: 16.1. LOGIC: Add 1 to the count of total closed ports
    # TODO: 16.2. OUTPUT: 127.0.0.1:80 is closed

    # TODO: 17. LOGIC: Check if return code is anything else
    # TODO: 17.1. LOGIC: Add 1 to the count of total unknown ports
    # TODO: 17.2. OUTPUT: 127.0.0.1:80 is unknown

    # TODO: 18. OUTPUT: Section Banner of Port Stats
    # TODO: 19. OUTPUT: Total Ports Scanned
    # TODO: 20. OUTPUT: Total Ports Open
    # TODO: 21. OUTPUT: Total Ports Closed
    # TODO: 22. OUTPUT: Total Ports Unknown

    pass
    
if __name__ == "__main__":
    main()