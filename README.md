# quotes-api
Briq - Python Developer coding challenge (Create quotes API)

## Installing dependencies
- Install dependencies with `pip install -r requirements.txt`

## Usage
- Open terminal in the `src` folder.
- Run `python excel_to_mongodb.py` to create and populate a collection in a MongoDB database with the data present in the given Excel spreadsheet. This needs to be done just once (already done).
- Run `python flask_application.py` and explore the available endpoints on your browser.

## Endpoints available
| Endpoint | Description | Example | isIdempotent |
|--|--|--|--|
| `/quotes/all` | Gets all quotes | Self explanatory | True |
| `/quotes/rated` | Gets only rated quotes  | Self explanatory | True |
| `/quotes/unrated` | Gets only unrated quotes | Self explanatory | True |
| `/quotes/recommended` | Gets only recommended quotes (quotes with rating > 3) | Self explanatory | True |
| `/quotes/similar_quotes?quote=<string>&top=<int>` | Gets quotes (from the recommended quotes collection) that are most similar to the quote given. |  `/quotes/similar_quotes?quote=someQuoteAboutSomething&top=20` | True |
| `/quote/add?quote=<string>` | Adds quote to the collection |  `/quote/add?quote=This is my new quote` | False |
| `/quote/delete?_id=<string>` | Deletes quote from the collection (based on unique ID) | `/quote/delete?_id=someUniqueId` | False |
| `/quote/update_rating?_id=<string>&new_rating=<float>` | Updates the rating of an already existing quote. Retrieves the quote by it's unique ID. | `/quote/update_rating?_id=someUniqueId&new_rating=4.3` | False |
| `/quote?_id=<string>` | Gets quote based on given ID. Returns empty dictionary if quote with given ID doesn't exist. | `/quote?_id=QCA9CCASSX5Y` | True |