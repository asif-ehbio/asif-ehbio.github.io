cat <<EOF > ehb_bot.py
import smtplib
from email.message import EmailMessage

# তোমার তথ্য
SENDER_EMAIL = "Ethicalhacker.bd.official@gmail.com"
APP_PASSWORD = "gvgj glwr huuo qpxy"

def send_official_email(receiver, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = f"EHB Official <{SENDER_EMAIL}>"
    msg['To'] = receiver
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ ইমেইল সফলভাবে পাঠানো হয়েছে: {receiver}")
    except Exception as e:
        print(f"❌ এরর: {e}")

if __name__ == "__main__":
    # এখানে যাকে পাঠাতে চাও তার ইমেইল, বিষয় এবং মেসেজ দাও
    to = "target-email@gmail.com" 
    sub = "Official Message from EHB"
    text = "এটি একটি অফিসিয়াল টেস্ট ইমেইল।"
    
    send_official_email(to, sub, text)
EOF
