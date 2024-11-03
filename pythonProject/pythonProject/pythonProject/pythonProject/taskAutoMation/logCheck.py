# import os
#
# # Function to create the required directory structure
# def create_batchjob_structure(base_path):
#     batch_jobs = ['batchjob1', 'batchjob2']
#     jobs_structure = [
#         '01_E',
#         '01_E_A1',
#         '02_D',
#         '02_D_A1',
#         '03_W',
#         '03_W_A1',
#     ]
#
#     for job in batch_jobs:
#         job_path = os.path.join(base_path, job)
#         os.makedirs(job_path, exist_ok=True)
#
#         for structure in jobs_structure:
#             folder_path = os.path.join(job_path, structure)
#             os.makedirs(folder_path, exist_ok=True)
#
#             for i in range(1, 8):  # Create EN1 to EN7 folders
#                 en_folder = os.path.join(folder_path, f'EN{i}')
#                 os.makedirs(en_folder, exist_ok=True)
#
#                 masterlogs_path = os.path.join(en_folder, 'MASTERLOGS')
#                 os.makedirs(masterlogs_path, exist_ok=True)
#
#                 # Create log files
#                 for log_number in range(1, 5):
#                     log_file_path = os.path.join(masterlogs_path, f'log{log_number}.txt')
#                     with open(log_file_path, 'w') as log_file:
#                         log_file.write(f'This is log file {log_number} in {structure}/EN{i}/MASTERLOGS\n')
#
# # Specify the base path where the batch jobs should be created
# base_path = r'D:\2024\100 day 100 learnings\pythonProject\pythonProject\pythonProject\pythonProject\taskAutoMation'  # Use a raw string to avoid escape characters
# create_batchjob_structure(base_path)
# Above code generate file structure


import os
from html import escape


def generate_html_table(root_directory):
    # Create the base HTML structure
    html = """
    <html>
    <head>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Last 4 Log Files from Each Folder and Environment</h2>
        <table>
            <tr>
                <th>Environment</th>
                <th>Folder</th>
                <th>File Name</th>
                <th>File Size (KB)</th>
            </tr>
    """

    # Traverse the directory structure
    for folder, _, _ in os.walk(root_directory):
        if 'MASTERLOGS' in folder:
            env = folder.split('/')[-2]  # Get environment name (EN1, EN2, etc.)
            log_files = sorted(os.listdir(folder), key=lambda x: os.path.getmtime(os.path.join(folder, x)),
                               reverse=True)

            # Get the last 4 log files
            last_4_logs = log_files[:4]

            for log_file in last_4_logs:
                file_path = os.path.join(folder, log_file)
                file_size = os.path.getsize(file_path) / 1024  # Size in KB

                # Append file details to the HTML table
                html += f"""
                <tr>
                    <td>{escape(env)}</td>
                    <td>{escape(folder)}</td>
                    <td>{escape(log_file)}</td>
                    <td>{file_size:.2f}</td>
                </tr>
                """

    # Close the HTML tags
    html += """
        </table>
    </body>
    </html>
    """

    return html


# Specify the root directory where the batch jobs are stored
root_directory = 'D:\2024\100 day 100 learnings\pythonProject\pythonProject\pythonProject\pythonProject\taskAutoMation\batchjob1'

# Generate the HTML table and save it to a file
html_content = generate_html_table(root_directory)
with open("log_files_table.html", "w") as file:
    file.write(html_content)

print("HTML table generated and saved as log_files_table.html.")
