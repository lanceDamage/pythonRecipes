# One area of exploration is pull down if an vulnerability is remote or local in nature. 
This information is embedded in the CVSS score, in the Attack Vector (AV) element. 
The AV can be N for network, or L for Local. 
For each CV, it would be nice to go online, look up that value, and return whether it is remote or local. 
This seems like an intensive operation to do for every CVE.
It would be nice to have a table of all CVEs that are remotely executable at any given time. 
I think this sort of work will require interacting with the NVD.
Interacting with the NVD is dependant on working with JSON or XML data. 
