class MaintenanceApplication:
    def __init__(self, data_processing_module):
        self.data_processing_module = data_processing_module
        self.latest_status = None
        self.scheduled_tasks = []

    def update_elevator_status(self, processed_data):
        self.latest_status = processed_data
        print(f"Elevator health score: {processed_data['health_score']}")

    def identify_maintenance_needs(self):
        if not self.latest_status:
            return []

        return self.latest_status["alerts"]

    def schedule_maintenance_tasks(self, maintenance_requirements):
        self.scheduled_tasks.extend(maintenance_requirements)
        for requirement in maintenance_requirements:
            print(f"Scheduled: {requirement}")


def setup(data_processing_module):
    return MaintenanceApplication(data_processing_module)
