import re;
import sys;
import subprocess;
from datetime import datetime as date;

if len(sys.argv) != 2:
	print "usage: " + sys.argv[0] + " process_name";
	sys.exit(1);

used_memory = 0;

p = subprocess.Popen("smem | grep " + sys.argv[1], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT);

for line in p.stdout.readlines():
	m = re.search('(.)+\s+(\d+)+\s+(\d+)+', line);
	used_memory += int(m.group(2));
	
print date.now().strftime('%Y-%m-%d %H:%M') + " " + str(used_memory);

