*COMPANY*:CODTECH IT SOLUTIONS

*NAME*:TAMMU SOWMYA

*INTERN ID*:CT06DL381

*DOMAIN*:CYBER SECURITY

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTOSH

Purpose

To assist in penetration testing by:

1. Scanning for open ports on a target IP.


2. Grabbing banners from services running on those ports.


3. Performing SSH brute-force login attempts using a provided username and a list of common passwords.Function Descriptions

1. scan_ports(target, ports)

Purpose: Checks which ports are open on the target IP.

How it works:

Iterates over a list of ports.

Attempts to connect using a TCP socket.

Returns a list of open ports.


Output: Console log showing whether each port is open or closed.


2. grab_banners(target, ports)

Purpose: Retrieves service banners (server info) from open ports.

How it works:

Connects to each open port.

Sends a simple HTTP request (HEAD / HTTP/1.1).

Tries to read and print the banner (first 100 characters).


Use: Helps identify the software/service running on a port, e.g., Apache, nginx, etc.


3. ssh_brute_force(host, port, username, password_list)

Purpose: Attempts SSH login using brute-force with a list of passwords.

How it works:

Uses the paramiko library to connect to SSH.

Tries each password in the provided list.

Stops on successful login.
