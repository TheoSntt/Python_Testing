from server import create_app
from locust import HttpUser, task, events

from utilities.json_handler import JSON_Handler
json_handler = JSON_Handler()

def _reset_json_file(file_name):
    """ Remove all entries with __Locust in name """
    file = json_handler.load_json(file_name)
    for key in file:
        if 'LOCUST__' in key['name']:
            file.remove(key)
    json_handler.save_json(file_name, file)

class ProjectPerfTest(HttpUser):

    # Create a competition and a club only for locust
    # This is done on the test_start event so it is only done once for all simulated users and not for each one
    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        json_handler.update_json("competitions", {"name": "LOCUST__COMP",
                                     "date": "2050-01-01 12:00:00",
                                     "numberOfPlaces": 500000})

        json_handler.update_json("clubs", {"id": "LOCUST__",
                              "name": "LOCUST__CLUB",
                              "email": "secretary@locustclub.fr",
                              "points": 500000})
    
    # Remove LOCUST club and comp from JSON
    # This is done on the test_stop event so it is only done once for all simulated users and not for each one
    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        _reset_json_file('clubs')
        _reset_json_file('competitions')

    # For all simulated user, log them as the club created for Locust, before launching the tasks
    def on_start(self):
        """Code to be executed before starting the test."""
        self.client.post("login", {"email": "secretary@locustclub.fr"})

    # For all simulated user, log them out after the test is stoped
    def on_stop(self):
        """Code to be executed after the test ends."""
        self.client.get("logout")

    @task
    def home(self):
        self.client.get("")

    @task
    def competitions(self):
        self.client.get("competitions")

    @task
    def book(self):
        self.client.get("book/LOCUST__COMP")
    
    @task
    def purchase(self):
        self.client.post("purchasePlaces", {"competition": "LOCUST__COMP",
                                            "club": "LOCUST__CLUB",
                                            "places": 1})

    @task
    def clubs(self):
        self.client.get("clubs")


if __name__ == "__main__":
    app = create_app({"LOCUST": True})
    app.run(debug=True)