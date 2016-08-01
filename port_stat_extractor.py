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
# Read the ports.txt file and generates an output with the probability distribution of each combination of ports
# Usage: cat ports.txt | ./port_stat_extractor.py > ../ports-distribution.csv

import sys
import operator



amount_of_hosts = 0
hosts = {}
for line in sys.stdin:
    parts = line.split()
    port_list = ''
    for part in parts:
        if 'open' in part:
            port_number = part.split('/')[0] + ';'
            port_list += port_number
    # Dont work in the final list with the hosts without ports
    if port_list == '':
        continue
    # Count the hosts without open ports in the total hosts
    amount_of_hosts += 1
    port_list = port_list[:-1]
    # Count how many combinations
    try:
        host = hosts[port_list]
        hosts[port_list] += 1
    except KeyError:
        hosts[port_list] = 1
# Compute percentage
total_amount_of_perc = 0
for host in hosts:
    amount = hosts[host]
    hosts[host] = float(amount)/float(amount_of_hosts)
    total_amount_of_perc += hosts[host]
# Output
#print 'Total amount of lines: {}'.format(amount_of_hosts)
#print 'Total amount of %: {}'.format(total_amount_of_perc)
print 'probability,ports_combination(;)'
for host in hosts:
    print '{:.10f},{}'.format(hosts[host],host)
