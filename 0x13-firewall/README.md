0x13-firewall

0.Blocking all incoming traffic
In this task I install UFW(Uncomplicated Firewall) and setting up rules on web-01

What is UFW?
- User-friendly interface for managing firewall rules on Linux system mostly used on Ubuntu and other Debian-based systems

How UFW works?
- UFW has a simplied process of configuring the firewall rules by providing straightforward commands. You can setup rules for allowing or denying  traffic based on ports, protocols, and IP addresses. When UFW is enabled, it applies the rules to 'iptable' to control the flow of incoming and outgoing network traffic.

Installing UFW on Ubuntu.

Update the package lists
-sudo apt update

Installing UFW
-sudo apt install ufw

Check UFW status
sudo ufw status


Configuring UFW

Allowing SSH
- sudo ufw allow ssh (port: 22)

Allowing HTTP and HTTPS Traffic:
- sudo ufw allow http (port: 80)
- sudo ufw allow https (port: 443)

Allowing specified port
- sudo ufw allow 22
- sudo ufw allow 80
- sudo ufw allow 443 

Denying a specified port
_ sudo ufw deny [port number]

Enabling UFW		Disabling UFW
- sudo ufw enable 	- sudo ufw disable

How to view your UFW rules?
- sudo ufw status verbose

Deleting a UFW Rule
- sudo ufw delete allow http

