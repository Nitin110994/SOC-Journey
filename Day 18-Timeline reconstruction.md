## Attack Timeline Reconstruction


Event Timeline


Initial stage	- Host 10.9.5.71 begins DNS queries for suspicious domain


DNS activity -	Multiple queries for www.thealnwickgarden.net


DNS response -	DNS server 10.9.5.1 returns No such name


Network connection -	Host 10.9.5.71 initiates TCP connection to 166.117.110.61


TCP handshake -	Connection established using port 80 (HTTP)


Malware communication -	HTTP POST request sent to /fshv/


Data transmission -	Encoded payload sent using application/x-www-form-urlencoded


Persistent communication -	~6039 packets exchanged over ~141 minutes


Outcome	Confirmed -  command-and-control communication consistent with XLoader malware



## Attack Timeline

| Stage | Description |
|---|---|
DNS Activity | Host 10.9.5.71 repeatedly queries suspicious domain |
External Connection | TCP connection established to 166.117.110.61 |
HTTP Communication | POST request sent to /fshv/ |
Data Transmission | Encoded payload transmitted |
C2 Activity | Persistent communication observed |


The investigation began when unusual DNS activity was observed from the internal host 10.9.5.71. The host repeatedly attempted to resolve the domain www.thealnwickgarden.net
, which returned multiple No such name responses. Shortly afterward, the host initiated a TCP connection to the external IP address 166.117.110.61 over port 80. Further inspection of the HTTP traffic revealed a POST request to /fshv/ containing encoded data. Analysis of the TCP stream confirmed that the infected host was transmitting data to the remote server. Conversation statistics showed over 6000 packets exchanged during a period of approximately 141 minutes, indicating sustained command-and-control communication consistent with XLoader malware activity.
