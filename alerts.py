import smtplib

def send_alert(ip):
    sender = "ap291495@gmail.com"     # change this
    receiver = "sorapalliajay@gmail.com"  # change this
    password = "Ajay@2002"  # use App Password (not normal password)

    subject = "🚨 Network Alert!"
    body = f"Suspicious activity detected from IP: {ip}"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
        print(f"[+] Alert email sent for {ip}")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")
