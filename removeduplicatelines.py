lines_seen = set() # holds lines already seen
outfile = open("tokenizerinput.txt", "w", encoding="utf8")
for line in open("ywdialogcleanupFINAL.txt", "r", encoding="utf8"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
for line in open("ywmapnpcdialogFINAL.txt", "r", encoding="utf8"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()