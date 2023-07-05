# 0x07.Networking Basic #0

## Learning objectives

> 1. OSI MODEL
> 2. LAN
> 3. WAN
> 4. What is the Internet
> 5. TCP/UDP

## OSI MODEL

> The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a communication system into seven distinct layers.

> It helps in understanding and describing how different network protocols and technologies interact to enable communication between networked devices. Each layer in the OSI model has a specific set of functions and responsibilities.

> The layers are:
* Application layer
* Presentation layer
* Session layer
* Transport layer
* Network layer
* Data link layer
* Physical layer

## LAN

> LAN stands for Local Area Network. It is a computer network that connects devices within a limited geographical area, such as a home, office building, or school campus. A LAN is designed to facilitate communication and resource sharing between devices in close proximity to each other.

### Typical Usage

> File and Resource Sharing: LANs enable users to share files, documents, printers, scanners, and other resources within the network. This allows for easy collaboration and access to shared resources.

> Local Application Hosting: LANs can host applications or services that are accessible to users within the network. For example, a LAN might host a local file server or a database server that is used by multiple devices.
> Internet Access Sharing: LANs often provide a gateway to the internet, allowing multiple devices within the network to share a single internet connection. This is commonly achieved through a router that connects the LAN to the internet.

> Local Multiplayer Gaming: LANs are popular for hosting local multiplayer gaming sessions. Players can connect their devices to the LAN and play games together, utilizing the low-latency and high-speed connectivity offered by the network.

### Typical Geographical Size

> The range of a LAN is typically limited to a few hundred meters to a few kilometers, and it is often confined to a single site or location. To connect multiple LANs together over a larger area, additional networking technologies like Wide Area Networks (WANs) or the internet may be used.

> Home Network: A LAN in a typical home network would cover the devices within the house or apartment.

> Office LAN: In an office environment, a LAN would typically cover a floor, a building, or a group of buildings in close proximity.

> School Campus: LANs in educational institutions, such as schools or universities, can cover an entire campus or a specific area within the campus.

## WAN

> WAN stands for Wide Area Network. It is a type of computer network that spans over a large geographical area, connecting multiple LANs or other networks together. Unlike LANs, which are confined to a limited area, WANs cover a wide geographic region, such as cities, countries, or even continents. 

> WANs are designed to facilitate communication and data exchange between geographically dispersed locations.

### Typical Usage

> Interconnecting Multiple LANs: WANs provide a means to connect multiple LANs together, enabling communication and resource sharing between different sites or locations. This is particularly useful for organizations with branch offices or multiple sites that need to share data and resources.

> Remote Access: WANs allow remote access to network resources. Users can connect to the corporate network from remote locations using technologies such as virtual private networks (VPNs) or dedicated connections, enabling secure access to resources and services.

> Internet Connectivity: WANs provide access to the internet for connected networks and devices. They allow organizations or individuals to connect to the global network of networks, enabling access to online services, websites, and cloud-based resources.

> Wide-Scale Data Transfer: WANs facilitate the transfer of large volumes of data between distant locations. This is especially important for industries such as finance, healthcare, and research, where large datasets need to be shared or synchronized across different sites.

### Typical Geographical Size

> WANs cover vast geographical areas and can span across cities, regions, countries, or even continents. The size of a WAN can vary depending on the specific requirements and scale of the network. Some examples of WANs include:
* Metropolitan Area Network (MAN): MANs cover a metropolitan area, such as a city or a large urban region. They interconnect multiple LANs within the city, enabling communication between different organizations or locations.
* Wide-Area Network Service (WAN Service): WAN services are provided by telecommunications companies and connect multiple locations across a wide geographic area. These services may use technologies like leased lines, MPLS (Multiprotocol Label Switching), or VPNs to establish connectivity.
* Global Wide Area Network: Some WANs span across continents or connect multiple countries together. These large-scale networks are often utilized by multinational corporations, international service providers, or research and education networks.

> The geographical size of a WAN can vary greatly, depending on the specific requirements and coverage area. WANs are built using a combination of networking technologies, such as routers, switches, dedicated circuits, and communication protocols, to establish connectivity and enable communication between the connected locations.

## What is the Internet?

> The Internet is a global network of interconnected computer networks. It consists of millions of private, public, academic, business, and government networks that are linked together using various technologies. It allows users to share and access information, communicate with others, and engage in various online activities like browsing websites, sending emails, and streaming videos.

### What is an IP address

>An IP (Internet Protocol) address is a unique numerical label assigned to each device connected to a computer network. It serves as an identifier for that device, allowing it to communicate with other devices over the Internet. IP addresses are used to route data packets between different devices and networks. There are two main versions of IP addresses in use today: IPv4 and IPv6.

* IPv4 (Internet Protocol version 4): This is the most widely used version of IP addresses. It consists of four sets of numbers, separated by periods (e.g., 192.168.0.1). Each set can range from 0 to 255, providing a total of approximately 4.3 billion unique addresses. However, due to the growing number of devices connected to the Internet, the availability of IPv4 addresses is becoming limited.
* IPv6 (Internet Protocol version 6): IPv6 was developed to address the limitations of IPv4 and provide a larger address space. IPv6 addresses are written as eight groups of four hexadecimal digits, separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334). This allows for a significantly larger number of unique addresses, ensuring that the increasing number of devices can be connected to the Internet.

### What is a localhost?

> Localhost is a hostname that refers to the current device or computer that you are using. It is used to access the network services running on the same device. When you access "localhost" in a web browser or use it in network communications, you are referring to the device you are currently using. It is often used for testing and development purposes.

### What is a subnet?

> A subnet (short for subnetwork) is a division of an IP network into smaller, logically separate networks. It helps in managing and organizing IP addresses within a larger network. By creating subnets, network administrators can control network traffic, improve security, and efficiently allocate IP addresses. Each subnet has its own range of IP addresses and can be treated as an independent network within the larger network infrastructure.

## TCP/UDP

> TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two transport layer protocols used for data transmission over IP networks.

> TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data packets. It establishes a connection between the sender and receiver before transmitting data and ensures that packets are delivered in the correct order. TCP also performs flow control and congestion control to manage the rate of data transmission.

> UDP is a connectionless protocol that provides a simple method for sending data packets without establishing a direct connection. Unlike TCP, UDP does not guarantee reliable delivery or packet ordering. It is often used for applications where speed and efficiency are more important than reliability, such as real-time streaming and online gaming.

> The main difference between TCP and UDP lies in their reliability and connection management. TCP is reliable and ensures that data is delivered in the correct order without errors. It establishes a connection, performs error checking, and retransmits lost packets. UDP, on the other hand, does not provide reliability mechanisms. It does not establish a connection and does not guarantee ordered or error-free delivery of packets. UDP is faster and more lightweight than TCP but sacrifices reliability.

### Port

> In networking, a port is a communication endpoint associated with a specific process or service on a device. It is identified by a unique number ranging from 0 to 65535. Ports allow multiple applications to use the same IP address on a device by distinguishing between different services. For example, web servers typically use port 80 for HTTP and port 443 for HTTPS.

### Tool/protocol to check device connectivity

> A commonly used tool/protocol to check if a device is connected to a network is the ICMP (Internet Control Message Protocol) Echo Request/Echo Reply, which is commonly known as "ping." By sending an ICMP Echo Request packet to a device's IP address, you can determine if the device is reachable and responsive. If the device is connected and functioning properly, it will send an ICMP Echo Reply packet back to the sender.
