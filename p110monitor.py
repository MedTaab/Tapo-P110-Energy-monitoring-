import curses
import datetime
import time
from PyP100 import PyP110

# Initialize PyP110 object with your TP-Link Smart Plug details
p110 = PyP110.P110("172.20.10.9", "medooutaabout2002@gmail.com", "med1234@H")
threshold=3000
# List to store power usage data
power_usage_data = []

def update_energy_statistics(stdscr, y=2):
    if power_usage_data:
        powers = [power for _, power in power_usage_data]
        min_power = min(powers) if powers else 0
        max_power = max(powers) if powers else 0
        avg_power = sum(powers) / len(powers) if powers else 0

        stdscr.addstr(y, 0, f"Lowest Energy Usage: {min_power:.2f} W")
        stdscr.addstr(y+1, 0, f"Highest Energy Usage: {max_power:.2f} W")
        stdscr.addstr(y+2, 0, f"Average Energy Usage: {avg_power:.2f} W")
        stdscr.refresh()

def get_device_info(stdscr):
    try:
        # Perform handshake and login if not already authenticated
        p110.handshake()
        p110.login()

        device_info = p110.getDeviceInfo()
        stdscr.addstr(6, 0, f"Device Info: {device_info}")  # Debugging
        stdscr.refresh()

        # Check the structure of device_info
        if isinstance(device_info, dict):
            if 'result' in device_info:
                device_data = device_info['result']
                if 'device_on' in device_data:
                    status = "On" if device_data['device_on'] else "Off"
                    stdscr.addstr(0, 0, f"Device Status: {status}")
                else:
                    stdscr.addstr(0, 0, "Device Status: Unknown")
            else:
                stdscr.addstr(0, 0, f"Device Info does not contain 'result' key: {device_info}")
        else:
            stdscr.addstr(0, 0, f"Device Info is not a dictionary: {device_info}")

        stdscr.refresh()

        try:
            energy_usage = p110.getEnergyUsage()
            stdscr.addstr(7, 0, f"Energy Usage: {energy_usage}")  # Debugging
            stdscr.refresh()

            if isinstance(energy_usage, dict):
                if 'result' in energy_usage and 'current_power' in energy_usage['result']:
                    current_power_watts = energy_usage['result']['current_power'] / 1000
                    stdscr.addstr(1, 0, f"Current Energy Usage: {current_power_watts:.2f} W")
                    current_time = datetime.datetime.now()
                    power_usage_data.append((current_time, current_power_watts))

                    update_energy_statistics(stdscr)
                else:
                    stdscr.addstr(1, 0, f"Energy Usage does not contain 'result' or 'current_power' key: {energy_usage}")
            else:
                stdscr.addstr(1, 0, f"Energy Usage is not a dictionary: {energy_usage}")

        except KeyError as e:
            stdscr.addstr(4, 0, f"KeyError in energy usage data: {e}")
        except Exception as e:
            stdscr.addstr(4, 0, f"Exception in energy usage data: {e}")

    except KeyError as e:
        stdscr.addstr(4, 0, f"KeyError in device information: {e}")
    except Exception as e:
        stdscr.addstr(4, 0, f"Exception in device information: {e}")

    stdscr.refresh()

def main(stdscr):
    # Configure curses settings
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input

    try:
        while True:
            stdscr.clear()
            get_device_info(stdscr)
            time.sleep(1)  # Adjust refresh rate here
    except KeyboardInterrupt:
        stdscr.addstr(10, 0, "Program interrupted. Exiting...")
        stdscr.refresh()
        time.sleep(2)

while True:
    power_consumption = get_power_consumption(device)
    print(f"Consommation actuelle : {power_consumption} W")
    if power_consumption > threshold:
        print(f"Seuil de {threshold} W dépassé. Extinction de la prise.")
        device.turn_off()
        break
    time.sleep(10)  # Vérifie toutes les 10 secondes

# Start curses application
curses.wrapper(main)
