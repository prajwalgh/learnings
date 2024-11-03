import subprocess


def check_task_status(task_name):
    try:
        # Run the schtasks command to query the status of the task
        result = subprocess.run(['schtasks', '/Query', '/TN', task_name, '/FO', 'LIST', '/V'], capture_output=True,
                                text=True)
        # print(result.stdout)
        # Check if the command ran successfully
        if result.returncode == 0:
            # Print the output or process it to extract the status
            output = result.stdout
            for line in output.splitlines():
                if "Status:" in line:
                    status = line.split(":", 1)[1].strip()
                    return status
        else:
            return f"Failed to query task: {result.stderr}"
    except Exception as e:
        return str(e)


# Example usage
task_name = r'\HPAudioSwitch'  # Specify your task name here
status = check_task_status(task_name)
print(f"Task Status: {status}")
