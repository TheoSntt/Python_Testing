# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Install and run the app

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Once that is done, you can run the app locally by using the following command <code>python server.py</code>


4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. Those are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing : running the tests

    To run all the unit and integration tests, you can use the command <code>pytest</code> or <code>pytest -v</code> if you want more details. All the tests should pass, confirming that the app has the expected behaviour in regard of the previous issues.

6. Testing : generating a coverage report

    To generate the coverage report, use the following command <code>pytest --cov=. --cov-report html</code>. It will regenerate the coverage report already available in the htmlcov folder. The coverage should be 83%.

7. Testing : running a performance test

    - Performance is measured using Locust. Follow these steps to run a performance test :

    - First, you need the launch the app in "locust mode" (which allows for booking more that 12 places per competition, which is needed to adequately measure the response time). To do so, use this command <code>python locustfile.py</code>

    - You can then, in another terminal, launch locust, by using the command <code>locust</code>

    - You can now open the Web interface at the indicated URL (http://localhost:8089/)

    - You can chose the test parameters. The host must be the one at which you are running the app (usually http://127.0.0.1:5000/). You will see that with up to 6 users (as per specified), the response times never get close to a full second.

