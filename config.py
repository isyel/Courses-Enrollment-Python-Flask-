import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x1c\xe9\x87~\x05\xb7V \x11W\xd2\x10q\xd7\xb3e'
    
    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment'}
    
    # MONGODB_SETTINGS = { 'db': 'UTA_Enrollment',
    #                     'host': 'mongodb:localhost:27017/UTA_Enrollment' }