from smtplib import SMTP
import email.mime.multipart, email.mime.text, email.mime.image
from bs4 import BeautifulSoup

host = {'host_id': 'smtp.gmail.com', 'port': 587 }
user_login = {'username': 'ljivesh4@gmail.com', 'password': '95689568'}

email_list = {
                'to_list':
                ['ljivesh4@gmail.com',
                 'ljivesh3@gmail.com',
                 'ljivesh@gmail.com',
                 'ljivesh6@gmail.com']
                ,
                'from_list':
                ['ljivesh4@gmail.com']

            }

html_source = open('MyBlog.html').read()


def email_parser(source, format):
    soup = BeautifulSoup(source, 'html.parser')

    for img in soup.find_all('img'):
        print(img.get('src'))
        image = email.mime.image.MIMEImage(open(img.get('src'), 'rb').read())
        image.add_header('Content-ID', '<'+img.get('src')+'>')
        format.attach(image)
        img['src'] = 'cid:' + img.get('src')
        print(img.get('src'))

    if soup.find('link').get('rel'):
        stylesheet = open(soup.find('link').get('href')).read()
        style_tag = soup.new_tag('style')
        style_tag.string = stylesheet
        soup.link.replace_with(style_tag)
        print(soup)

    return soup

def Send_HTML(html_source):

    print(html_source)

    email_conn = SMTP(host['host_id'], host['port'])
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(user_login['username'], user_login['password'])

    email_format = email.mime.multipart.MIMEMultipart('alternative')
    email_format['Subject'] = "Hello There"
    email_format['From'] = ", ".join(email_list['from_list'])
    email_format['To'] = ", ".join(email_list['to_list'])
    new_html_source = email_parser(html_source, email_format)
    email_format.attach(email.mime.text.MIMEText(new_html_source, 'html'))

    email_conn.sendmail(email_list['from_list'], email_list['to_list'], email_format.as_string())
    email_conn.quit()

    print("Success!!")

if __name__ == '__main__':
    Send_HTML(html_source)
