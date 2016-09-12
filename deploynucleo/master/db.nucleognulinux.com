;
; BIND data file for local loopback interface
;
$ORIGIN nucleognulinux.com.
$TTL	604800
@	IN	SOA	dns1.nucleognulinux.com. root.nucleognulinux.com. (
			      2		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
	IN	NS	dns1.nucleognulinux.com.
	IN	NS	dns2.nucleognulinux.com.
dns1		A	192.168.1.124
dns2		A	192.168.1.125
server	IN	A	192.168.1.153
router	IN	CNAME	server
www	IN	CNAME	server
ftp	IN	CNAME	server
