from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch,Comment
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('run',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User ,Pitch = Pitch )


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

    
if __name__ == '__main__':
    manager.run()