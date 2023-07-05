0x08. Networking basics #1
==========================

-   By Terry Wambui
-   Weight: 1


![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png)

## Learning Objectives

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine's active network interfaces

### What is localhost/127.0.0.1

> "Localhost" is a hostname that is used to refer to the current device or computer that you are using. It is commonly associated with the IP address "127.0.0.1."

> When you access "localhost" in a web browser or use it in network communications, you are referring to the device you are currently using. It is often used for testing and development purposes. Any services or applications running on the device can be accessed through the localhost address.

> The IP address "127.0.0.1" is a loopback address that is reserved for the purpose of communication within the device itself. When a program or service communicates with "127.0.0.1," it is essentially sending data to itself. This loopback mechanism allows developers to test and debug applications locally without the need for an external network connection.

### What is 0.0.0.0

> The IP address "0.0.0.0" has a special meaning in networking. It is known as an "unspecified" or "wildcard" address.

> When a device is assigned the IP address "0.0.0.0," it typically indicates that the device does not have a specific assigned IP address or it is not yet configured with a valid IP address. It can also be used to represent all IP addresses on the local machine or on a particular network interface.

> In some cases, network administrators may use the IP address "0.0.0.0" to configure network services or applications to listen on all available network interfaces or to bind to any available IP address. This allows the services or applications to accept connections from any source IP address.

> Overall, the IP address "0.0.0.0" is a placeholder that represents various meanings depending on the context in which it is used, such as indicating the absence of a specific IP address or representing all available IP addresses.

### What is /etc/hosts

> The /etc/hosts file is a plain text file found in Unix-like operating systems (including Linux) that serves as a local DNS (Domain Name System) lookup table. It maps hostnames to IP addresses on the local machine.

> When a computer needs to communicate with another computer on a network, it typically uses the DNS to translate human-readable domain names (like www.example.com) into IP addresses (like 192.0.2.1). The /etc/hosts file provides a way to override or supplement the DNS lookup process by defining custom mappings between hostnames and IP addresses locally.

> By modifying the /etc/hosts file, you can define custom hostname-to-IP address mappings on your local machine. This can be useful for testing or development purposes, or for overriding DNS resolution for specific domains. When a program on the machine tries to access a hostname listed in the /etc/hosts file, it will use the associated IP address defined in the file instead of querying a DNS server.

### How to display your machine's active network interfaces

> ifconfig: This command displays information about all active network interfaces on your Linux machine, including their IP addresses, MAC addresses, and other details. However, newer Linux distributions often use the ip command instead of ifconfig.

> ip addr show: This command provides similar information as ifconfig but is considered more modern and is available on newer Linux systems.
