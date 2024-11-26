# internet-archive-flashcards
This is the backend of a flashcard app that uses Flask and MongoDB. 
There's a one time webscraper included in app/scripts that scrapes from Internet Archive Bookreader to collect data.
Internet Archive Bookreader is a fantastic service, and I very much appreciate them. These flashcards are for personal use, so it respects their terms of service!
The initial book is Speak Québec! From Page 29 on by Daniel Kraus. 
Then after that, the flashcard api will randomly select from the flashcards in the database and provide the translation after. 
Front end coming. 
Still a work in progress, but we have functionality in the flashcard api. 
There will be an auth login just for fun, even though the app is just for me. 




* python -m venv venv
* source venv/bin/activate
* deactivate
* pip install -r requirements.txt
* pip show internetarchive

* which python
* switch interpreter to that one

* ia configure