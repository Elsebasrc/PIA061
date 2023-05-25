import nmap
scaner = nmap.PortScanner()
scaner.scan('192.168.227.130','1-1024','-v -sV')
scaner.command_line() 
scaner.all_hosts() 
scaner[' 192.168.227.130'].state() 
scaner['192.168.227.130'].all_protocols()
scaner[ '192.168.227.130']['tcp'].keys() 
scaner['192.168.227.130'].has_tcp(21)
scaner['192.168.227.130'].has_tcp(22)
scaner[ '192.168.227.130'].tcp[22] 
scaner[ '192.168.227.130'].tcp[22][product]