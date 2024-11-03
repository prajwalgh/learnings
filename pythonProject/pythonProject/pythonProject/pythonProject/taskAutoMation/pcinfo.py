import platform
import subprocess
import shutil
import sys


def get_system_info():
    # Get basic system information
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version,
    }
    return system_info


def get_disk_space():
    # Get disk space information
    total, used, free = shutil.disk_usage("/")
    return {
        "Total": f"{total / (1024 ** 3):.2f} GB",
        "Used": f"{used / (1024 ** 3):.2f} GB",
        "Free": f"{free / (1024 ** 3):.2f} GB"
    }


def get_cpu_info():
    # Get CPU usage based on the platform
    try:
        if platform.system() == "Windows":
            result = subprocess.run(['wmic', 'cpu', 'get', 'LoadPercentage'], capture_output=True, text=True)
        else:  # Linux/Mac
            result = subprocess.run(['lscpu'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error retrieving CPU info: {str(e)}"


def get_memory_info():
    # Get memory usage information based on the platform
    try:
        if platform.system() == "Windows":
            result = subprocess.run(['wmic', 'OS', 'get', 'FreePhysicalMemory,TotalVisibleMemorySize'],
                                    capture_output=True, text=True)
        else:  # Linux/Mac
            result = subprocess.run(['free', '-h'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error retrieving memory info: {str(e)}"


def get_network_info():
    # Get network information based on the platform
    try:
        if platform.system() == "Windows":
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        else:  # Linux/Mac
            result = subprocess.run(['ifconfig'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error retrieving network info: {str(e)}"


def main():
    print("System Information:")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    print("\nDisk Space Info:")
    for key, value in get_disk_space().items():
        print(f"{key}: {value}")

    print("\nCPU Info:")
    print(get_cpu_info())

    print("\nMemory Info:")
    print(get_memory_info())

    print("\nNetwork Info:")
    print(get_network_info())


if __name__ == "__main__":
    main()
