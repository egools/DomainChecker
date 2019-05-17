import os
import csv
#import dns.resolver

def checkHost(hostname):
    response = os.system("ping -n 1 " + hostname)
    return response == 0

#print(dns.resolver.query("sc.rr.com", "MX"))

with open("TotalDomainsChecked.csv", mode="w", newline="") as checkedCSV:
    fieldnames = ["domain", "valid"]
    writer = csv.writer(checkedCSV)
    writer.writerow(fieldnames)

    with open("TotalDomains.csv", "r") as domains:
        domain = domains.readline().rstrip()
        while domain:
            writer.writerow([domain, checkHost(domain)])
            domain = domains.readline().rstrip()
    
    