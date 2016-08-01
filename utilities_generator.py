#!/usr/bin/env python
#  Copyright (C) 2016  Sebastian Garcia
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Authors:
# Sebastian Garcia eldraco@gmail.com

# Description
# Reads the ports.csv file and the port_attractivness.csv file and generates the utilities for the GM

import math

company_index = 10000

# ports.csv has the list of ~1000 ports scanned by nmap
file_ports = open('ports.csv')
file_attr = open('port_attractivness.csv')

# Store the list of ports we work with in memory
ports_attractivness = []
for line in file_attr:
    if 'port' in line or '#' in line:
        continue
    ports_attractivness.append(line)

print '# Numbers represent potential money U$S in July 2016'
print '# 0- Port'
print '# 1- target_value: The value of the assets in this port. Positive number. The money the attacker gets for attacking a real port successfully. (e.g. 2000)'
print '# 2- Honeypot_deployment_cost: Deployment cost for the defender of 1 honeyport. Very low, very. Positive. (e.g. 5)'
print '# 3- Honeypot_interaction_cost: Cost for the defender of an attacker attacking the honeypot for real and abusing it. The risk that you fuck up the honeypot security. Not so much, but something. (e.g. 100)'
print '# 4- Attacker_loss_honeypot: What the attacker loses for interacting with a honeypot. That is, being detected, being blocked, reveling 0-days, potential going to jail. Positive. (e.g. 300)'
print '#'
print '# Ratios'
print '# Each company has an index level in direct relationship with its economic grow, e.g. NASDAQ. The index is called X'
print '# 1 = X'
print '# 2 = 0.0001 * x'
print '# 3 = 0.01 * x'
print '# 4 = x * 0.05'
print 'port, target_value, honeypot_deployment_cost, honeypot_interaction_cost, attacker_loss_honeypot'

for line in file_ports:
    if 'port' in line:
        continue
    port = int(line.strip())
    # is port in the list of port attractivness?
    #print 'Is port {} in the file?'.format(port)
    is_there = False
    target_value = 0.0
    honeypot_deployment_cost = 0.0
    honeypot_interaction_cost = 0.0
    attacker_loss_honeypot = 0.0
    for line in ports_attractivness:
        #print 'First port {}, second {} '.format(str(port), str(line.split(',')[0]))
        # a_ for analyzed
        a_port = int(line.split(',')[0].strip())
        a_attr = float(line.split(',')[1].strip())
        if port == a_port:
            # print 'It is: {}'.format(line)
            # x * attractivness
            target_value = float(company_index * a_attr) 
            # x * 0.0001
            honeypot_deployment_cost = 0.0001 * company_index
            honeypot_interaction_cost = 0.01 * company_index
            #attacker_loss_honeypot = math.log(company_index + 1)
            # Attacker's lose if he is being detected is 5% of company value
            attacker_loss_honeypot = company_index * 5.0 / 100.0
            is_there = True
            break
    if not is_there:
        # print 'Port {} is not there!'.format(port)
        # Default attractivness if the port is not known
        a_attr = 0.01
    target_value = float(company_index * a_attr)
    honeypot_deployment_cost = 0.0001 * company_index
    honeypot_interaction_cost = 0.01 * company_index
    #attacker_loss_honeypot = math.log(company_index + 1) 
    # Attacker's lose if he is being detected is 5% of company value
    attacker_loss_honeypot = company_index * 5.0 / 100.0
    #print 'Port: {}'.format(port)
    #print 'Attractivness: {}'.format(attr)
    # output
    print '{},{},{},{},{}'.format(port,target_value,honeypot_deployment_cost,honeypot_interaction_cost, attacker_loss_honeypot)


