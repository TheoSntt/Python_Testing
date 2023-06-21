from tests.conftest import client


# def test_should_status_code_ok(client):
# 	response = client.get('/index')
# 	assert response.status_code == 200
	
# def test_should_return_hello_world(client):
# 	response = client.get('/index')
# 	data = response.data.decode() #Permet de décoder la data dans la requête
# 	assert data == 'Hello, World!'

# def test_registration_page_should_status_code_ok(client):
#     response = client.get('/')
#     assert response.status_code == 200

# def test_registration_valid_email_should_status_code_ok(client):
#     response = client.post('/showSummary', data={'email' : 'admin@irontemple.com'})
#     assert response.status_code == 200

# def test_registration_invalid_email_should_status_code_ok(client):
#     response = client.post('/showSummary', data={'email' : 'bad@email.com'})
#     assert response.status_code == 200

# def test_registration_valid_email_should_get_summary_page(client):
#     response = client.post('/showSummary', data={'email' : 'admin@irontemple.com'})
#     data = response.data.decode()
#     assert data.find("Summary | GUDLFT Registration") != -1

# def test_registration_invalid_email_should_get_invalid_account_page(client):
#     response = client.post('/showSummary', data={'email' : 'bad@email.com'})
#     data = response.data.decode()
#     assert data.find("GUDLFT Registration - Invalid Account") != -1
    

# def test_booking_right_amount_of_places_should_be_allowed(client):
#     # Connecting a user
#     response = client.post('/showSummary', data={'email' : 'admin@irontemple.com'})
#     data = response.data.decode()
#     assert data.find("Summary | GUDLFT Registration") != -1
#     # Can purchase places
#     response = client.post('/purchasePlaces', data={'places' : '2',
#                                                     'club' : "Iron Temple",
#                                                     'competition' : "Spring Festival"})
#     assert response.status_code == 200
#     data = response.data.decode()
#     assert data.find('Great-booking complete!') != -1


# def test_booking_more_places_than_available_points_should_not_be_allowed(client):
#     # Connecting a user
#     response = client.post('/showSummary', data={'email' : 'admin@irontemple.com'})
#     data = response.data.decode()
#     assert data.find("Summary | GUDLFT Registration") != -1
#     # Can purchase places
#     response = client.post('/purchasePlaces', data={'places' : '7',
#                                                     'club' : "Iron Temple",
#                                                     'competition' : "Spring Festival"})
#     assert response.status_code == 200
#     data = response.data.decode()
#     print(data)
#     assert data.find("You do not have enough points to book that many places") != -1


# def test_places_booked_should_be_deduced_from_points(client):
#     # Connecting a user
#     response = client.post('/showSummary', data={'email' : 'admin@irontemple.com'})
#     data = response.data.decode()
#     assert data.find("Summary | GUDLFT Registration") != -1
#     # Get club
#     # club = [c for c in clubs if c['name'] == request.form['club']][0]
#     response = client.post('/purchasePlaces', data={'places' : '2',
#                                                     'club' : "Iron Temple",
#                                                     'competition' : "Spring Festival"})
#     assert response.status_code == 200
#     data = response.data.decode()
#     assert data.find('Great-booking complete!') != -1