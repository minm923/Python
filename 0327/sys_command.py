import subprocess;
subprocess.check_call("ls -lh .", shell=True)
a = subprocess.check_output("ls -lh .", shell=True)
print 'a = %s' % a
