#!/bin/bash

echo "Вы запустили скрипт: $0"

echo "Введите массу тела (в кг):"
read weight

echo "Введите рост (в сантиметрах):"
read height 

if [ -z "$weight" ] || [ -z "$height" ]; then
    echo "Ошибка: масса и рост не могут быть пустыми."
    exit 1
fi

bmi=$((weight * 10000 / height / height))	

echo "Ваш индекс массы тела (BMI): $bmi"
