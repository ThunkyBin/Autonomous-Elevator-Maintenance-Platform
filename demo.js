const readings = {
  devicesOnline: 2,
  sensorCount: 3,
  vibration: 7.4,
  temperature: 41.2,
  doorCycles: 1820,
};

const alerts = [];

if (readings.vibration > 6.5) {
  alerts.push("Inspect traction motor vibration");
}

if (readings.temperature > 40) {
  alerts.push("Check machine-room ventilation");
}

if (readings.doorCycles > 1500) {
  alerts.push("Schedule door mechanism inspection");
}

const healthScore = Math.max(0, 100 - alerts.length * 18);

console.log("Autonomous Elevator Maintenance Demo");
console.log(`Devices online: ${readings.devicesOnline}`);
console.log(`Sensors connected: ${readings.sensorCount}`);
console.log(`Elevator health score: ${healthScore}`);

if (alerts.length === 0) {
  console.log("No maintenance tasks required.");
} else {
  for (const alert of alerts) {
    console.log(`Notification sent: ${alert}`);
    console.log(`Scheduled: ${alert}`);
  }
}
