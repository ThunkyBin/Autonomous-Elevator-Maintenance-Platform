class DataCollectionModule:
    def __init__(self, devices, sensors):
        self.devices = devices
        self.sensors = sensors

    def collect_data(self):
        return {
            "devices_online": sum(1 for device in self.devices if device["status"] == "online"),
            "sensor_count": len(self.sensors),
            "vibration": 7.4,
            "temperature": 41.2,
            "door_cycles": 1820,
        }


def setup(devices, sensors):
    return DataCollectionModule(devices, sensors)
