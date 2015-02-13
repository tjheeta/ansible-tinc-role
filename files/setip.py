#!/usr/bin/env python

try:
    import netaddr
except Exception, e:
    raise errors.AnsibleFilterError('python-netaddr package is not installed')

import fnmatch
import os
import sys

dir_pubkey=sys.argv[1]
dir_ip=sys.argv[2]
subnet_str=sys.argv[3]
subnet=netaddr.IPNetwork(subnet_str)
subnet_list=list(subnet.iter_hosts())

matches = []
for root, dirnames, filenames in os.walk(dir_pubkey):
    for filename in fnmatch.filter(filenames, '*'):
        matches.append(filename)

ip_list={}
for name in matches:
    file_path=os.path.join(dir_ip, name)
    if os.path.exists(file_path):
        ip=open(file_path).readline().rstrip()
        ip_list[name] = ip
    else:
        ip_list[name] = 0

for k,v in ip_list.iteritems():
    if v == 0:
        # find an untaken ip address in subnet
        used_ip_list = map(netaddr.IPAddress, ip_list.values())
        new_ip_list = sorted(list(set(subnet_list) - set(used_ip_list)))
         
        if len(new_ip_list) > 0:
            ip_list[k] = str(new_ip_list[0])
        else:
            sys.stderr.write('Cannot get an IP address in subnet')

for k,v in ip_list.iteritems():
    file_path=os.path.join(dir_ip, k)
    cur_file=open(file_path, 'w')
    cur_file.write( v )
    cur_file.close()

print ip_list
