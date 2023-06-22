import json
from flask import abort, Flask, render_template, request, redirect, flash, url_for, session
from utilities.json_handler import JSON_Handler
from utilities.booking_helper import Booking_Helper


# def loadClubs():
#     with open('db/clubs.json') as c:
#          listOfClubs = json.load(c)['clubs']
#          return listOfClubs


# def loadCompetitions():
#     with open('db/competitions.json') as comps:
#          listOfCompetitions = json.load(comps)['competitions']
#          return listOfCompetitions

# json_handler = JSON_Handler()

# def loadCompetitions():
#     json_handler.loadCompetitions()

# def loadClubs():
#     json_handler.loadClubs()

# competitions = loadCompetitions()
# clubs = loadClubs()


def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object(config)
    json_handler = JSON_Handler()
    booking_helper = Booking_Helper()

    # def loadCompetitions():
    #     json_handler.loadCompetitions()
    
    # def loadClubs():
    #     json_handler.loadClubs()

    competitions = json_handler.loadCompetitions()
    clubs = json_handler.loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['POST'])
    def login():
        try:
            for club in clubs:
                print(club['email'])
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            session['logged_club'] = club
            return redirect(url_for('show_competitions'))
        except IndexError:
            flash(f"No account exists with this mail : '{request.form['email']}'", "flash_error")
            return redirect(url_for('index'))

    # @app.route('/showSummary',methods=['POST'])
    # def showSummary():
    #     try:
    #         club = [club for club in clubs if club['email'] == request.form['email']][0]
    #     except IndexError:
    #         return render_template('invalid_account.html')
    #         # abort(403)
    #     return render_template('competitions.html',club=club,competitions=competitions)

    @app.route('/competitions')
    def show_competitions():
        if 'logged_club' in session:
            return render_template('competitions.html', club=session['logged_club'], competitions=competitions)
        else:
            flash("You need to be logged to access this page", "flash_warning")
            return redirect(url_for('index'))

    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            maximum = booking_helper.max_places_allowed(foundCompetition, foundClub)
            return render_template('booking.html',club=foundClub,competition=foundCompetition, max_places=maximum)
        else:
            flash("Something went wrong-please try again")
            return render_template('competitions.html', club=club, competitions=competitions)

    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        # Here the number of places asked is deducted from the number of places of the competition
        # But it is not deducted from the clubs points, and wether there is enough point is not checked
        # Let's add this control
        if placesRequired <= booking_helper.max_places_allowed(competition, club):
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            flash('Great-booking complete!', 'flash_info')
        else:
            flash(f"You can only book a maximum of "
                    f"{booking_helper.max_places_allowed(competition, club)}"
                    " places",
                    'flash_warning')
        return render_template('competitions.html', club=club, competitions=competitions)


    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))


    return app




if __name__ == "__main__":
    app = create_app({"TESTING": False})
    app.run(debug=True)