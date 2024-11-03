# # import schedule
# # import time
# # import io
# # import sys
# # import win32com.client as win32
# #
# # # Define your function
# # def my_function():
# #     # Example function output
# #     output = "This is the output of the function."
# #     print(output)
# #     return output
# #
# # # Function to capture the output of my_function
# # def run_function():
# #     # Redirect standard output
# #     old_stdout = sys.stdout
# #     sys.stdout = new_stdout = io.StringIO()
# #
# #     # Run the function
# #     try:
# #         result = my_function()
# #     finally:
# #         # Restore standard output
# #         sys.stdout = old_stdout
# #
# #     # Get the output and return it
# #     output = new_stdout.getvalue()
# #     return output
# #
# # # Function to send email using Outlook
# # def send_email(subject, body):
# #     outlook = win32.Dispatch('outlook.application')
# #     mail = outlook.CreateItem(0)
# #     mail.To = 'prajwalgaidhani18@gmail.com'
# #     mail.Subject = subject
# #     mail.Body = body
# #     mail.Send()
# #
# # # Function to run the main function and send the output via email
# # def run_and_notify():
# #     output = run_function()
# #     send_email('Function Output', output)
# #
# # # Run the task immediately
# # run_and_notify()
# #
# # # Schedule the task to run daily at 9:25 AM
# # # schedule.every().day.at("09:25").do(run_and_notify)
# # #
# # # # Keep the script running
# # # while True:
# # #     schedule.run_pending()
# # #     time.sleep(1)
#
#
# import win32com.client as win32
# import logging
#
# # Configure logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# def send_test_email():
#     try:
#         logging.debug("Creating Outlook application instance.")
#         # Create an instance of the Outlook application
#         outlook = win32.Dispatch('outlook.application')
#
#         logging.debug("Creating a new mail item.")
#         # Create a new email item
#         mail = outlook.CreateItem(0)
#
#         # Set the recipient, subject, and body of the email
#         mail.To = 'prajwalgaidhani18@gmail.com'
#         mail.Subject = 'Test Email'
#         mail.Body = 'This is a test email sent from a Python script using Outlook.'
#
#         logging.debug("Sending the email.")
#         # Send the email
#         mail.Send()
#
#         logging.info("Test email sent successfully!")
#     except Exception as e:
#         logging.error("An error occurred: %s", e)
#
#
# # Call the function to send the test email
# send_test_email()

import win32com.client as win32

olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

# construct email item object
mailItem = olApp.CreateItem(0)
mailItem.Subject = 'Hello 123'
mailItem.BodyFormat = 1
mailItem.Body = 'Hello There'
mailItem.To = 'prajwalgaidhani18@gmail.com'
mailItem.Sensitivity  = 2
# optional (account you want to use to send the email)
# mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('<email@gmail.com')))
mailItem.Display()
# mailItem.Save()
# mailItem.Send()