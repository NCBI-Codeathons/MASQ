import sys
for line in sys.stdin:
    if line.startswith("##"):
        sys.stdout.write(line)
    elif line.startswith("#"):
        sys.stdout.write(line.strip() + "\tFORMAT\tSAMPLE\n")
    else:
        sys.stdout.write(line.strip() + "\t.\t.\n")

