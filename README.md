Sets up tinc as a mesh network. It will setup all ip addresses and setup hosts file entries. For instance, if tinc_netname is mesh, all the nodes will have entries host1.mesh, host2.mesh, etc. Also, for a private mesh, you can specify multiple entries of tinc_connectto.

Requirements: 

python-netaddr must be installed

Runit must be installed either manually or through a package or precompiled binaries: 
https://github.com/tjheeta/ansible-runit-role

Variables:

```
tinc_netname: mesh               # what the domainname that hostsfile will refer to
tinc_connectto:                  # what public hosts that can be connected to
   publichost1: 1.2.3.4
   publichost2: 1.2.3.5
tinc_subnet: 10.11.0.0/24        # what public hosts that can be connected to
tinc_port: 2005                  # tinc port
tinc_state: present              # whether this mesh name is present or not
tinc_static_binary: true         # whether to use the included binaries
```

