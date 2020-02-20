#!/usr/bin/env python
from __future__ import (print_function, absolute_import, division, unicode_literals)
import socket
import subprocess
import ipaddress

# json is not alway default installed, if json is not installed simplejson is installed
# for this reason python will check is json is installed or it will fallback to simplejson
try:
    import json
except ImportError:
    import simplejson as json

def inventory():
    """ function: create a dynamicly generated inventory for ansible """
    ipaddrs = find_nodes()
    return {
            'all': {
                'hosts': [ipaddrs],
                'vars': {},
                },
            '_meta': {
                'hostvars': {
                    'ipaddrs': {
                        'ansible_ssh_user': 'ansible',
                        'ansible_host': [ipaddrs],
                        'ansible_port': '19131',
                        }
                    },
               },
            'nodes': [ipaddrs]
        }	

def find_nodes():
    """ function: return ipaddress in you local network where port 22 is open """
    ipaddres = list()
    for ip in all_local_ipaddrs():
        if ssh_is_open(str(ip)):
            ipaddres.append(str(ip))

#        if port_22_is_open(str(ip)):
#            ipaddres.append(str(ip))
    return ipaddres	

def all_local_ipaddrs():
    """ function: find all active ipaddress in your local network """
    my_net = ipaddress.ip_network(u'192.168.0.0/24')
    for ipaddr in my_net.hosts():
        yield ipaddr	

def ssh_is_open(ipaddr):
    """ function: check if port 22 is open """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ipaddr, 19131))
    sock.close()
    return result == 0

def port_22_is_open(ipaddr):
    """ function: check if port 22 is open """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ipaddr, 22))
    sock.close()
    return result == 0

def main():
    """ function: main function for returning the dynamic inventory """
    print('{}' .format(json.dumps(inventory(), sort_keys=True, indent=2)))

if __name__ == "__main__":
    main()
