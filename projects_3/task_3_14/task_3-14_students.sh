#!/bin/bash

echo 'Имена:'
awk '{print $1}' students.txt

echo 'Оценки:'
awk '{print $2}' students.txt

echo 'Номер строки:'
awk '{print NR, $1}' students.txt
