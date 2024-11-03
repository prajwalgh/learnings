import os

def get_last_four_files(base_path):
    # Store the data for the HTML table
    data = []

    # Loop through each batch job folder
    for job in ['batchjob1', 'batchjob2']:
        job_path = os.path.join(base_path, job)

        # Loop through the specified EN folders
        for folder in ['01_E', '01_E_A1', '02_D', '02_D_A1', '03_W', '03_W_A1']:
            folder_path = os.path.join(job_path, folder)

            for i in range(1, 8):  # Loop through EN1 to EN7
                en_folder = os.path.join(folder_path, f'EN{i}')
                masterlogs_path = os.path.join(en_folder, 'MASTERLOGS')

                if os.path.exists(masterlogs_path):
                    # Get all log files in the MASTERLOGS folder
                    log_files = [f for f in os.listdir(masterlogs_path) if f.endswith('.txt')]
                    log_files.sort(key=lambda x: os.path.getmtime(os.path.join(masterlogs_path, x)), reverse=True)  # Sort by modification time

                    # Get the last 4 files and their sizes
                    for file_name in log_files[:4]:  # Last 4 files
                        file_path = os.path.join(masterlogs_path, file_name)
                        size = os.path.getsize(file_path)  # Get file size in bytes
                        data.append((job, folder, f'EN{i}', file_name, size))

    return data

def generate_html_table(data):
    # Start the HTML table
    html_content = '''
    <html>
        <head>
            <title>File Sizes</title>
            <style>
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid black; padding: 8px; text-align: center; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2>Last 4 File Names and Sizes</h2>
            <table>
                <tr>
                    <th>Batch Job</th>
                    <th>Folder</th>
                    <th>EN Folder</th>
                    <th>File Name</th>
                    <th>Size (bytes)</th>
                </tr>
    '''

    # Add rows to the HTML table
    for job, folder, en_folder, file_name, size in data:
        html_content += f'''
                <tr>
                    <td>{job}</td>
                    <td>{folder}</td>
                    <td>{en_folder}</td>
                    <td>{file_name}</td>
                    <td>{size}</td>
                </tr>
        '''

    # Close the HTML tags
    html_content += '''
            </table>
        </body>
    </html>
    '''

    # Write the HTML to a file
    with open('file_sizes.html', 'w') as f:
        f.write(html_content)

def main():
    base_path = r'D:\2024\100 day 100 learnings\pythonProject\pythonProject\pythonProject\pythonProject\taskAutoMation'  # Change this to your base path
    last_four_files_data = get_last_four_files(base_path)
    generate_html_table(last_four_files_data)
    print("HTML table generated successfully.")

if __name__ == '__main__':
    main()
