import time
from tplinkcloud import TPLinkDeviceManager

# Configuration
username = 'medooutaabout2002@gmail.com'
password = 'med1234@H'
device_alias = 'Smart Plug'
threshold = 3000  # Remplacez X par le seuil de puissance en watts

# Initialisation de l'API
manager = TPLinkDeviceManager(username, password)
manager.update_device_list()
device = manager.get_device_by_alias(device_alias)

def get_power_consumption(device):
    emeter = device.get_emeter_realtime()
    power = emeter['power_mw'] / 1000  # Conversion en watts
    return power

while True:
    power_consumption = get_power_consumption(device)
    print(f"Consommation actuelle : {power_consumption} W")
    if power_consumption > threshold:
        print(f"Seuil de {threshold} W dépassé. Extinction de la prise.")
        device.turn_off()
        break
    time.sleep(10)  # Vérifie toutes les 10 secondes
