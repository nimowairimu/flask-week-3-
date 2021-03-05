import os



class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nimo:kadesho62@localhost/pitch34'
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nimo:kadesho62@localhost/pitch34'
    DEBUG = True

    # os.environ.get("DATABASE_URL")

config_options = {
'development':DevConfig,
'production':ProdConfig,
}