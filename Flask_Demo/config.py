

SECRET_KEY = "adnfifkhkafafjjkfaj"

#数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = "root"
PASSWORD = '123456'
DATABASE = "maohu"
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


#邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "3240175569@qq.com"
MAIL_PASSWORD = "edkfiucbtbpecgja"
MAIL_DEFAULT_SENDER = "3240175569@qq.com"
#edkfiucbtbpecgja