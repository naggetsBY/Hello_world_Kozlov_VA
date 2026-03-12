#!/bin/bash

echo "Файл A T G C"

for file in *.fasta; do
    echo "$file $(grep -o A "$file" | wc -l) $(grep -o T "$file" | wc -l) $(grep -o G "$file" | wc -l) $(grep -o C "$file" | wc -l)"
done

