import subprocess
import re

network_range = "172.16.43.0/24"

print(f"Iniciando varredura de rede na rede {network_range}...")

result = subprocess.run(["nmap", "-sn", "-n", network_range], capture_output=True, text=True)

nmap_output = result.stdout

print(nmap_output)

hosts_descobertos = re.findall(r"Nmap scan report for (?:.+ \()?([\d\.]+)\)?", nmap_output)

print("Hosts ativos encontrados:")
for host in hosts_descobertos:
    print(f" - {host}")