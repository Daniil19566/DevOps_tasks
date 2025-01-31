#!/bin/bash

echo " Запуск проекта DevOps_tasks..."
echo "Проверка зависимостей..."

# Проверка установленного Git
if ! command -v git &> /dev/null; then
    echo " Git не установлен! Установите его перед продолжением."
    exit 1
else
    echo " Git установлен!"
fi

# Вывод версии проекта
VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
echo " Текущая версия проекта: $VERSION"

echo " Всё готово к работе!"
