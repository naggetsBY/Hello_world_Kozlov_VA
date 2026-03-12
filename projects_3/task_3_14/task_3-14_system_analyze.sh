#!/bin/bash

df -h | awk 'NR>1 {
    print $1, $5
    if ($5 > 90) {
        print "ПРЕДУПРЕЖДЕНИЕ: " $1 " заполнен на " $5
    }
}'
