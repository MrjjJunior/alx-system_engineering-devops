#0x14-mysql

login to web-01

installed mysql on web-01 and web-02
$sudo apt install mysql-server

when i run mysql in CLI I get an error message
message:
	"ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)"

I went to dev.mysql.com and copied the PGP PUBLIC KEY

I pasted the key to file named mysql_v5.7.key

ran command:
	~$ sudo apt-key add mysql_v5.7.key
	~$ sudo apt update
	~$ sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'


#version check
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.36-0ubuntu0.20.04.1
  Version table:
     8.0.36-0ubuntu0.20.04.1 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages

not getting the version 5.7 mysqli 
