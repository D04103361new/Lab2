#!/usr/bin/env python

from json import dumps
import shlex, subprocess

def grep(target, s):
	print(target.split("\n"))
	for line in target.split("\n"):
	    pos = line.find(s)
	    if pos!= -1:
		return line[pos:]
		
def ip():
	cmd = '''
		ip addr show dev eth0
	'''
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdout=subprocess.PIPE)
	output = p.communicate()[0]
	ipaddr=""
	if output:
		s = grep(output, 'inet')
		pos = s.find('/')
		ipaddr = s[5:pos]
	return ipaddr
	
def hostname():
	cmd = '''
		hostname
	'''
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdout=subprocess.PIPE)
	output = p.communicate()[0]
	return output.strip()

def cpu():
        cmd = '''
                cat /proc/cpuinfo
        '''
        args = shlex.split(cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        output = p.communicate()[0]
        cpuaddr=""
        if output:
            s = grep(output, 'processor')
            pos = s.find(', ')
            cpuaddr = s[pos]
        return cpuaddr

def memory():
        cmd = '''
                awk '$3=="kB"{$2=$2/1024;$3="GB"} 1' /proc/meminfo
        '''
        args = shlex.split(cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        output = p.communicate()[0]
        memoryaddr=""
        if output:
            s = grep(output, 'MemTotal:')
            pos = s.find(', ''MemFree:')
            memoryaddr = s[10:pos]
        return memoryaddr
	
def main():
	host_stats = {}
	host_stats['ip'] = ip()
	host_stats['hostname'] = hostname()
        host_stats['cpu'] = cpu()
        host_stats['memory'] = memory()
	print(dumps(host_stats))
	
if __name__ == '__main__':
	main()
