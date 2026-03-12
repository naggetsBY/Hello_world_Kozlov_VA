#!/bin/bash	

if [ $# -lt 2 ]; then
    echo "Ошибка: недостаточно входящих данных."
    echo "Использование: $0 <имя_гена> <уровень_экспрессии>"
    exit 1
fi

gene_name="$1"
expression_level="$2"

echo "Экспрессия гена $gene_name составляет $expression_level единиц"	
