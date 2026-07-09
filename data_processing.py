class DataProcessingModule:
    def process_data(self, data):
        alerts = []

        if data["vibration"] > 6.5:
            alerts.append("Inspect traction motor vibration")

        if data["temperature"] > 40:
            alerts.append("Check machine-room ventilation")

        if data["door_cycles"] > 1500:
            alerts.append("Schedule door mechanism inspection")

        return {
            **data,
            "health_score": max(0, 100 - len(alerts) * 18),
            "alerts": alerts,
        }


def setup():
    return DataProcessingModule()
