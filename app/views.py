from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect


default_blueprint = Blueprint('default', __name__, url_prefix='/')


@default_blueprint.route('')
def index():
    return render_template('index.html')



    # @app.route("/thankyou")
    # def thankyou():
    #     return render_template('thankyou.html')

def send_link_as_mail(**kwargs):
    subject = 'New Visitor - Brookfield Consultants'

    msg = Message(subject, sender='rbagbai@aigbusiness.com', recipients=[
        'pkaur@aigbusiness.com'
    ])

    msg.html = """Please click on the link below to sign your probation status form.<br>
    <a href="http://{0}/document/{1}/{2}">Click here</a>
    """.format(request.host,kwargs['rev_emp_code'],kwargs['emp_code'])

    mail.send(msg)

@default_blueprint.route("/thankyou" , methods=['POST'])
def thankyou():
    name = request.form.get('name')
    email = request.form.get('email')
    msg = request.form.get('msg')
    print(email)
    return render_template('thankyou.html', name=name, email=email, msg=msg)