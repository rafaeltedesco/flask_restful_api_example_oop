from server import TaskApi
from resources.tasks_api.tasks import Tasks
from resources.persons_api.persons import Persons
from resources.main.home import Home

if __name__ == '__main__':
    api = TaskApi()
    api.add_resource(Home, '/')
    api.add_resource(Tasks, '/tasks')
    api.add_resource(Persons, '/persons')
    api.start(debug=True)
