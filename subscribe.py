# modules
from pygnmi.client import gNMIclient, telemetryParser

# variables
from inventory import hosts

#body

for host_entry in hosts:
    if host_entry["nos"]  == "arista-eos":

        subscribe = {
            'subscription':[
                {
                    'path': 'openconfig-interfaces:interfaces/interface[name=Ethernet1]',
                    'mode' : 'sample',
                    'sample_interval': 1000000000
                },

                {
                    'path': 'openconfig-interfaces:interfaces/interface[name=Management1]',
                    'mode' : 'sample',
                    'sample_interval': 1000000000
                }

            ],

            # 'use_aliases': false,
            'mode': 'stream',
            'encoding': 'proto'
        }


        with gNMIclient(target=(host_entry["ip_address"], host_entry["port"]),
                        username= host_entry["username"], password= host_entry["password"], insecure = True) as gc:

                    #collect telemetry
             telemetry_stream = gc.subscribe(subscribe=subscribe) #creates telemetry stream

             for telemetry_entry in telemetry_stream:
               print(host_entry)