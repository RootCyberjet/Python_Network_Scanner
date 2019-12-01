#****************************************************************
#                   NAME - SHIBA BISWAS
#                   DESIGNATION - STUDENT
#                   EMAIL - shibabiswas1111@gmail.com
#                   INDIA
#****************************************************************


#! /usr/bin/python

import socket
import optparse
import sys
import timeit
from datetime import *


print("----------------------------------------------")
print("Current time : "+str(datetime.now()))
print("----------------------------------------------")


def sock_creation(target_host1, target_port1):
    
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except s.error as msg1:
            print("Socket creation error : "+str(msg1))

        try: 
            s.connect((target_host1, int(target_port1)))
            service = socket.getservbyport(int(target_port1),'tcp')
            p = [ str(target_port1)+"/TCP", "open", service]
            print('{:>8} {:>8} {:>16}'.format(*p))
            s.close()
        except:
            service = "NOT AVAILABLE"
            p = [ str(target_port1)+"/TCP", "closed", service]
            print('{:>8} {:>8} {:>16}'.format(*p))
            
#****************************************************************

def port_scan(target_host,target_ports):
    try:
        target_IP = socket.gethostbyname(target_host)
    except:
        print("Target host IP can't resolve.")
        sys.exit(0)

    print("              PORT SCANNING                   ")
    print("----------------------------------------------")
    print("For PORT scanning of : "+target_IP+'('+target_host+')')
    print("----------------------------------------------")
    print("    PORT     STATUS        SERVICE ")
    print("----------------------------------------------")
    for port in target_ports:
        sock_creation(target_IP,port)
    print("----------------------------------------------")

#****************************************************************

start = timeit.default_timer()
parser = optparse.OptionParser('program_name -H <target_host> -P <target_port>')
parser.add_option('-H', dest='host', type='string', help='Enter target host.')
parser.add_option('-P', dest='port', type='string', help='Enter target port/ports(separated by ",").')
(options, args) = parser.parse_args()
target_host = options.host
target_port = str(options.port).split(',')
if target_host == None or target_port[0] == None:
    print('Enter Target Host & Target Port.')
    sys.exit(0)
port_scan(target_host,target_port)
stop = timeit.default_timer()
T=stop-start
print("----------------------------------------------")
print("Scanning is complete.")
print("Total Scanning Time : "+str(T)+" sec.")
print("----------------------------------------------")

#****************************************************************


