# Architecture

The platform is organized around a small set of modules:

- IoT device setup
- Sensor setup
- Data collection
- Data processing
- Maintenance decision logic
- Notification delivery

`AutonomousElevatorMaintenancePlatform` wires these modules together and runs a
monitoring loop. Each loop collects elevator data, processes it, updates the
maintenance status, and sends notifications when maintenance is required.
