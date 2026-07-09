class NotificationSystem:
    def send_notifications(self, maintenance_requirements):
        for requirement in maintenance_requirements:
            print(f"Notification sent: {requirement}")


def setup():
    return NotificationSystem()
