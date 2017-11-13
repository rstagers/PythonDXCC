import re

telnet_output = 'DX de K7XC:       3525.0  VK9MA        CQ CW CQing up1 Tnx QSO!  VK9M 0748Z NV'

callsign_pattern = "([a-z|0-9|/]+)"
frequency_pattern = "([0-9|.]+)"
pattern = re.compile("^DX de "+callsign_pattern+":\s+"+frequency_pattern+"\s+"+callsign_pattern+"\s+(.*)\s+(\d{4}Z)", re.IGNORECASE)

match = pattern.match(telnet_output)

if match:
	spotter = match.group(1)
	frequency = float(match.group(2))
	spotted = match.group(3)
	comment = match.group(4).strip()
	spot_time = match.group(5)
#	band = frequency_to_band(frequency)

print(spotter, frequency, spotted, comment, spot_time)

'''
I believe that the only way to get the prefix is to go through the DX call and iteriate 
through the call checking the prefix.  an example is VK9MA...

V = Nothing
VK = Australia
VK9 = Norfolk Island
VK9M = Mellish Island 
VK9MA = Nothing

So for this call the prefix is VK9M...  and the entity is Mellish Island
Seems a bit weird to have to do it this way but my poor brain can't see any other
way at the moment. 

Have to watch for stupid calls as well...  PJ4/K9VD would be an example...
No idea about a K9VD/DL1 type of call if that is even possible!

The spot network that I am on gives the prefix for DX calls not US or Canada
for those it give the dang state or provance in the tail end of the comments 
string.  So if I start at the end of the string and get the chars up to the first 
space and compare with the DX call; this should be the prefix.  Will have to test 
all this out or jsut use it and when it fails figure out why.  

Sad nothing is documented in the HAM radio world!
   
''' 
