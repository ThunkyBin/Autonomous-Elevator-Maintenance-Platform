# Autonomous Elevator Maintenance Platform

Prototype platform for monitoring elevator performance with IoT devices,
sensors, data processing modules, maintenance scheduling, and notifications.

## Features

- Real-time elevator performance monitoring
- Sensor and IoT data collection
- Maintenance requirement detection
- Automated maintenance task scheduling
- Notification flow for maintenance updates
- Modular structure for future integrations

## Main Script

`autonomous_elevator_maintenance.py` wires the platform modules together and
runs the monitoring loop.

## Documentation

- [Getting Started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Contact And Support](docs/contact-and-support.md)

## Run

Local Node demo:

```bash
npm start
```

Python prototype:

```bash
python autonomous_elevator_maintenance.py --once
```

## Notes

The Python prototype includes lightweight local modules for IoT devices,
sensors, data collection, data processing, maintenance scheduling, and
notifications. The Node demo mirrors the same monitoring cycle for environments
where Python is not installed.
