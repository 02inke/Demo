from flask import Blueprint,render_template,jsonify,redirect,url_for,session
from exts import mail,db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel,UserModel
from .forms import ResgisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash        #password加密



bp = Blueprint("author",__name__,url_prefix="/author")

@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱未注册!!!")
                return redirect(url_for("author.login"))
            if check_password_hash(user.password,password):
                #cookie:一般存放登录授权的thing
                #flask中的session是经过加密后存储cookie中
                session['user_id'] = user.id
                return redirect('/')
            else:
                print("密码错误!!")
                return redirect(url_for("author.login"))
        else:
            print(form.errors)
            return redirect(url_for("author.login"))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("author.login"))




@bp.route('/register',methods=['GET',"POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        #表单验证：flask-wtf
        form = ResgisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("author.login"))

        else:
            print(form.errors)
            return redirect(url_for("author.register"))


@bp.route("/captcha/email")
def captcha_email():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source,4)
    captcha = "".join(captcha)
    message = Message(subject="验证码",recipients=[email],body=f"验证码是:{captcha}")
    mail.send(message)
    #验证码通过数据库存储
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    #RESTful API
    #{code:200/400/500,message:"",data:{}}
    return jsonify({"code":200,"message":"","data":None})


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试",recipients=["zhihao_z@126.com"],body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功!"