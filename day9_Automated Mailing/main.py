import faker
import os
import yagmail




#user and password are get in envorment varbale with name USER18_GMAIL and USER18_GMAILPASSWORD
USER=os.environ.get('USER18_GMAIL')
PASSWORD=os.environ.get('USER18_GMAILPASSWORD')
def generate_email(n)->list:
    fake = faker.Faker()
    emails = []
    for _ in range(n):
        email = fake.email()
        emails.append(email)
    return emails

def send_email(email):
    yag=yagmail.SMTP(USER,PASSWORD)
    content=['test1','test2','test3']
    yag.send(email,'testing',content)

def main():
    emails=generate_email(2)
    for emails in emails:
        send_email(emails)

if __name__ == '__main__':
    main()

