#!/bin/bash

for i in {1..10}; do
    touch "test$i.txt"
done

i=10
while [ $i -gt 0 ]; do
    rm "test$i.txt"
    i=$((i-1))
done

