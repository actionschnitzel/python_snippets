import psutil
import time

def get_size(bytes, suffix="B"):
    # unit conversion
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_stats():
    # Line break
    print("=" * 40, "CPU Info", "=" * 40)

    # CPU frequencies
    CPU_Frequency = psutil.cpu_freq()
    print(f"Current Frequency: {CPU_Frequency.current:.2f}Mhz")

    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Line break
    print("=" * 40, "Memory Information", "=" * 40)

    # Memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print(f"Available: {get_size(svmem.available)}")

    # Line break
    print("=" * 40, "Disk Information", "=" * 40)
    print("Partitions and Usage:")

    # Disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")


if __name__ == "__main__":
    while True:
        time.sleep(2) # sleep for 2 seconds
        get_stats()