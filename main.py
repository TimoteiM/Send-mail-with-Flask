from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'moscaliuctimotei@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        subject = request.form.get('mailsub')
        text = request.form.get('bodymsg')
        recipient = request.form.get('sentto')
        msg = Message(subject,
                      sender='moscaliuctimotei@gmail.com',
                      recipients=[recipient])
        msg.body = text
        mail.send(msg)
        return "Sent email."
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)