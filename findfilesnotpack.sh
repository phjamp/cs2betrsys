#!/bin/bash
cat /var/lib/dpkg/info/*.{list,conffiles} | sort | uniq  > filespack.txt
find /* -type f | sort | uniq > allfiles.txt
diff allfiles.txt filespack.txt > diff.txt
