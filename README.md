# flask-week-3-
## Author
> Irene Wairimu Mungai, A student at Moringa School.
  There were no contributors apart from Irene Mungai only.

## Description
This is a web application that allows various users to submit a one minute pitch. Users can also be able to view other pitches from different categories ie Enterpreneurship, Interview and Sales, comment on the pitches posted and vote. 

## User Stories
* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.
## Specifications

| Behaviour  |	Input       |	  Output      |
|------------|--------------|-----------------|
|To Sign up | Click Sign up | Registers a new user into the application |
|To Sign In | Click Sign In | For sers who already have accounts to sign into the app|
|Display Various Pitch Categories|	N/A	|Various pitches grouped by categories are displayed|
|Display pitches |	Click on a Category	|A page with a list of pitches from the selected category|
|Add new pitch |	'Click To Pitch' |	User Should register/sign in to add new pitch|
|View Pitches |Click on a pitch	category|View a pitch,add upvote,downvote and comments|

## Prerequisites
Python3.6
## Setup Instructions
``git clone https://github.com/nimowairimu/flask-week-3-.git``
`` cd Pitches``
`` python3.6 -m venv virtual`` (install virtual environment)
`` source virtual/bin/activate``To activate the virtual environment
``python3.6 -m pip install -r requirements.txt``  To install all dependencies.
1.  Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
`` ./start.sh`` To run the application on your local server 


## How Pitch App  works
A user needs to sign up to the Pitch App
A user the needs to sign in
See the various categories there are of Pitches 
Give a vote for the Pitches 
Post their own Pitches in any category picked.

## Contacts Informantion
 - You can provide feedback or raise any issues/ bugs through my [Email](nimowairimu@gmail.com)
  - Or you can call me on my [Cell](+254704529132)


## Known Bugs
No known bugs of the Application.

## Technologies Used
* Python3.6
* Flask framework
* Bootstrap
* PostgreSQL
## License
MIT (c) 2021 Wairimu Mungai
