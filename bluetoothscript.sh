#!/bin/bash

# Функция для подключения к Bluetooth устройству
connect_bluetooth() {
    local device=$1
    bluetoothctl << EOF
    connect $device
EOF
}

# Проверка, включен ли Bluetooth
enabled=$(bluetoothctl show | grep "Powered: yes")

if [ -n "$enabled" ]; then
    echo "Bluetooth включен"
    
    # Показать список доступных устройств
    echo "Список доступных устройств:"
    bluetoothctl devices
    
    # Запросить у пользователя выбор устройства
    read -p "Введите MAC-адрес устройства, к которому хотите подключиться: " device_mac
    
    # Попытка подключения к выбранному устройству
    connect_bluetooth $device_mac
else
    echo "Bluetooth выключен. Включаем..."
    bluetoothctl power on
    echo "Bluetooth включен. Пожалуйста, запустите скрипт заново."
fi
