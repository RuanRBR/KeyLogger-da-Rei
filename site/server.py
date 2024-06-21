from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        with open("log.txt", "a") as log_file:
            log_file.write(f'{data["id"]}: {data["key"]}\n')
        
        if data["id"] == "username" and "@" in data["key"]:
            send_email(data["key"])
        elif data["id"] == "emailNotification":
            send_email(data["key"])

        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        return

def send_email(to_address):
    from_address = "chocomilkado.a@gmail.com"
    subject = "Rei Chiquita com Choco Milk"
    body = "Obrigado por se inscrever! Aqui está uma foto da Rei Chiquita com Choco Milk."
    
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    filename = "rei-gracias.png"
    attachment = open(filename, "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, "qiwyxtusiobekbjt")
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
