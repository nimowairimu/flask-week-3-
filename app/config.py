class Config:
    '''
    General configuration parent class
    '''

class ProdConfig(Config):
    '''
    Production config child class
    '''
    pass 

class DevConfig(Config):
    '''
    Development config child class
    '''

    DEBUG = True  
     
config_options = {
'development':DevConfig,
'production':ProdConfig
}