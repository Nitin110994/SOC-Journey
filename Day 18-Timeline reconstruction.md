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



Visual Attack Flow

Infected Host (10.9.5.71)
        │
        │ DNS Queries
        ▼
DNS Server (10.9.5.1)

        │
        │ TCP Connection
        ▼
External Server (166.117.110.61)

        │
        │ HTTP POST /fshv/
        ▼
Command & Control Communication

## Attack Timeline

| Stage | Description |
|---|---|
DNS Activity | Host 10.9.5.71 repeatedly queries suspicious domain |
External Connection | TCP connection established to 166.117.110.61 |
HTTP Communication | POST request sent to /fshv/ |
Data Transmission | Encoded payload transmitted |
C2 Activity | Persistent communication observed |

