import time
import psutil

# Define warning thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0


def monitor_system():
  print("--- Starting System Health Check ---")

  # 1. Check CPU Usage
  cpu_usage = psutil.cpu_percent(interval=1)
  print(f"CPU Usage: {cpu_usage}%")
  if cpu_usage > CPU_THRESHOLD:
    print(
        f"[ALERT] High CPU usage detected! ({cpu_usage}% >"
        f" {CPU_THRESHOLD}%)[span_2](start_span)[span_2](end_span)"
    )

  # 2. Check Memory Usage
  memory = psutil.virtual_memory()
  print(f"Memory Usage: {memory.percent}%")
  if memory.percent > MEMORY_THRESHOLD:
    print(
        f"[ALERT] High Memory usage detected! ({memory.percent}% >"
        f" {MEMORY_THRESHOLD}%)[span_3](start_span)[span_3](end_span)"
    )

  # 3. Check Disk Usage
  disk = psutil.disk_usage("/")
  print(f"Disk Usage: {disk.percent}%")
  if disk.percent > DISK_THRESHOLD:
    print(
        f"[ALERT] High Disk usage detected! ({disk.percent}% >"
        f" {DISK_THRESHOLD}%)[span_4](start_span)[span_4](end_span)"
    )

  print("--- System Health Check Complete ---")


if __name__ == "__main__":
  monitor_system()