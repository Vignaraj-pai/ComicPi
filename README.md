# GDSC Task - Responsive Landing Page

This a responsive home page for a comic reseller.

### The project uses Django framework to handle API calls.

## To run the server: 
  1) Clone the Repository
  2) run : ```$ cd gamepi```
  3) run : ```$ python manage.py runserver```
     + if this fails then:
     Run: ```$ pip install django```
     and try 3 again.
     + Click on the server link generated, which will look something like this: http://127.0.0.1:8000/
    Navigate to http://127.0.0.1:8000/home

## About the project:
  1) There is a Responsive collapsible navigation bar at the top, that sticks to the top when scrolling.
  2) The hero section contains some recent comic events that redirects to the particular resources
      + The hero section carousel has a bug - cannot change slides
  3) The next section contains a resonsive grid of recent comics
      + Clicking on any comic will create a popup with further options about the particular comic - [PENDING]
  4) The last section is the footer of the webpage.
