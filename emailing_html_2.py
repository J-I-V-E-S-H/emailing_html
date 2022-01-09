from smtplib import SMTP
import email.mime.multipart, email.mime.text, email.mime.image
from bs4 import BeautifulSoup
import os

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




def email_parser(source, format, path):
    soup = BeautifulSoup(source, 'html.parser')

    for img in soup.find_all('img'):
        print(img.get('src'))
        image = email.mime.image.MIMEImage(open(path + '/' + img.get('src'), 'rb').read())
        image.add_header('Content-ID', '<'+img.get('src')+'>')
        format.attach(image)
        img['src'] = 'cid:' + img.get('src')
        print(img.get('src'))

    if soup.find('link').get('rel'):
        stylesheet = open(path + '/' + soup.find('link').get('href')).read()
        style_tag = soup.new_tag('style')
        style_tag.string = stylesheet
        soup.link.replace_with(style_tag)
        print(soup)

    return soup

def Send_HTML(username, password, path, list, host_id, host_port):

    html_source = open(path+'/'+os.path.basename(path)+'.html').read()
    print(html_source)

    email_conn = SMTP(host_id, host_port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)

    email_format = email.mime.multipart.MIMEMultipart('alternative')
    email_format['Subject'] = "Hello There"
    email_format['From'] = ", ".join(username)
    email_format['To'] = ", ".join(list)
    new_html_source = email_parser(html_source, email_format, path)
    email_format.attach(email.mime.text.MIMEText(new_html_source, 'html'))

    email_conn.sendmail(username, list, email_format.as_string())
    email_conn.quit()

    print("Success!!")

if __name__ == '__main__':

    Send_HTML(user_login['username'], user_login['password'], html_source, email_list['to_list'], host['host_id'], host['port'])
