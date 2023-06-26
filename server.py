import json
from flask import abort, Flask, render_template, request, redirect, flash, url_for, session
from utilities.json_handler import JSON_Handler
from utilities.booking_helper import Booking_Helper



def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object(config)
    json_handler = JSON_Handler()
    booking_helper = Booking_Helper()
    _MAX_PLACES_PER_COMP = 12

    competitions = json_handler.load_json('competitions')
    clubs = json_handler.load_json('clubs')

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
            maximum = booking_helper.max_places_allowed(foundCompetition, foundClub, _MAX_PLACES_PER_COMP)
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
        print(placesRequired)
        print(booking_helper.max_places_allowed(competition, club, _MAX_PLACES_PER_COMP))
        if placesRequired <= booking_helper.max_places_allowed(competition, club, _MAX_PLACES_PER_COMP):
            # Remove the number of places booked from the competition
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            """
            # Remove the number of places booked from the club's points
            club['points'] = int(club['points']) - placesRequired
            """
            # Store the number of places booked by this club for this competition, so that the limit of 12 splaces
            # booked is respected even with multiple requests (like booking 5 places, then 5 more, then 5 more).
            # Add (or update if it preexists) a new entry in the competition dict with the clubs ID as a key and 
            # the number of booked places as a value.
            if club['id'] in competition:
                competition[club['id']] = int(competition[club['id']]) + placesRequired
            else:
                competition[club['id']] = placesRequired
            # Save both JSON files
            json_handler.update_json('competitions', competition)
            """
            json_handler.update_json('clubs', club)
            """
            # Confirmation message
            flash('Great-booking complete!', 'flash_info')
        else:
            flash(f"You can only book a maximum of "
                    f"{booking_helper.max_places_allowed(competition, club, _MAX_PLACES_PER_COMP)}"
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