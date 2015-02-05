# This file is only here to debug. Ultimately I merged the contents inline with 
# the archey bash script because calling another file while symlinking it 
# (my unique setup) became kind of onerous.
# If there's a simple fix to that, I'll gladly take it. Until then, sorry :(

import subprocess,re # standard stuff
import bitmath # someday I won't bother with this. Until, then, pip install ...

def getDriveStats():
  output=subprocess.Popen("df -k".split(),stdout=subprocess.PIPE)
  result=output.communicate()[0]
  return re.findall("(?:disk\S+\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+)",result)

result=[map(lambda x:bitmath.parse_string(x+"KiB"),n) for n in getDriveStats()]

total,used=map(lambda x:reduce(lambda y,z:y+z,x),zip(*result)) # Am I overcomplicating this?

print "{:.2%} of {:,.2f} TB".format(used/total,float(total.to_TB()))