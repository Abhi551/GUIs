import sys
import subprocess
s2_out = subprocess.check_output([sys.executable, "s2.py", "34"])
print s2_out