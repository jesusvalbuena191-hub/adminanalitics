class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/adminanalyticsdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

      # DB adicional (registrosmintic para PR, IM, fases_dda_2)
    SQLALCHEMY_BINDS = {
        'registrosmintic': 'mysql+pymysql://root:@localhost/registrosmintic'
    }