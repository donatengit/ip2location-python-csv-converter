import os, sys, logging
from netaddr import IPNetwork, IPSet, IPAddress

script_name = os.path.basename(sys.argv[0])

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(script_name)

if len(sys.argv) < 3:
    print(f"Usage: \n./{script_name} output_file merge_file_1 merge_file_2 ..merge_file_N")
    raise FileNotFoundError("Incorrect script usage, no arguments provided, please check.")

ip_ranges = IPSet()

output_file = open(f"{sys.argv[1]}", "w")
log.info("Starting reading CIDR ranges...")
for f in range(2, len(sys.argv)):
    log.info(f"File: {sys.argv[f]}")
    with open(sys.argv[f], "r") as in_file:
        for ip_range_or_address in in_file:
            if len(ip_range_or_address) == 0: continue
            ip_range_or_address = ip_range_or_address.strip()
            log.debug(f"Processing {ip_range_or_address}")
            try:
                if '/' in ip_range_or_address:
                    ip_ranges |= IPNetwork(ip_range_or_address)
                else:
                    ip_ranges |= IPAddress(ip_range_or_address)
            except Exception as oe:
                log.warning(f"Exception on reading/parsing ({oe}) on line '{ip_range_or_address}', skipping")
#log.info(f"Read {len(ip_ranges)} IP addresses. Merging...")

# ip_ranges.compact()

log.info(f"Resulting ip ranges: {ip_ranges}")

#log.info(f"{len(ip_ranges)} IP addresses after merge. Writing...")

for cidr in ip_ranges.iter_cidrs():
    output_file.write(f"{cidr}\n")

output_file.close()

log.info(f"All done.")
