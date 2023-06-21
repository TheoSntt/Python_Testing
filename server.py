import json
from flask import abort, Flask, render_template, request, redirect, flash, url_for, session
from utilities.json_handler import JSON_Handler


# def loadClubs():
#     with open('db/clubs.json') as c:
#          listOfClubs = json.load(c)['clubs']
#          return listOfClubs


# def loadCompetitions():
#     with open('db/competitions.json') as comps:
#          listOfCompetitions = json.load(comps)['competitions']
#          return listOfCompetitions



def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object(config)
    json_handler = JSON_Handler()

    competitions = json_handler.loadCompetitions()
    clubs = json_handler.loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['POST'])
    def login():
        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            session['logged_club'] = club
            return redirect(url_for('show_competitions'))
        except IndexError:
            flash(f"Sorry, '{request.form['email']}' wasn't found", "flash_error")
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
            flash("This action needs to be logged", "flash_warning")
            return redirect(url_for('index'))



    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('competitions.html', club=club, competitions=competitions)


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        flash('Great-booking complete!')
        return render_template('competitions.html', club=club, competitions=competitions)


    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))


    return app




if __name__ == "__main__":
    app = create_app({"TESTING": False})
    app.run(debug=True)