#!/bin/bash
 grep -o "sample" file* | sort | uniq -c | sed -e 's/^[ \t]*//'| cut -d ' ' -f2 | cut -d: -f1 | xargs grep -o "CSC510"|sort | uniq -c | sort -rn | grep -E "[3-9] file" |  sed -e 's/^[ \t]*//'| cut -d: -f1 | xargs -I {} sh -c 'size=$(stat -c "%s" $(echo {} | cut -d" " -f2)); echo "{} $size"'| sort -nr -k1,1 -k3,3 | cut -d ' ' -f2 | sed 's/file_/filtered_/'
