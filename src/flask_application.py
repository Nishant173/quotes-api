from flask import Flask, jsonify, request
import config
import crud_ops
import filters
import utils

app = Flask(__name__)

@app.route(rule='/', methods=['GET'])
def home():
    return "<h1>This is the Home page</h1>"


@app.route(rule='/quotes/all', methods=['GET'])
def all_quotes():
    return jsonify(utils.get_all_posts_from_mongodb(collection_name=config.MONGODB_COLLECTION_QUOTES))


@app.route(rule='/quotes/<string:filter_by>', methods=['GET'])
def filtered_quotes(filter_by):
    """NOTE: Filter options are: ['rated', 'unrated', 'recommended']"""
    filter_by = str(filter_by).lower().strip()
    if filter_by == "rated":
        return jsonify(filters.get_rated_posts())
    if filter_by == "unrated":
        return jsonify(filters.get_unrated_posts())
    if filter_by == "recommended":
        return jsonify(filters.get_recommended_posts())
    raise ValueError("Invalid endpoint. Expected one of ['quotes/rated', 'quotes/unrated', 'quotes/recommended']")


@app.route(rule='/quote', methods=['GET'])
def get_quote_by_id():
    quote_id = request.args['_id']
    quote = filters.get_quote_by_id(quote_id=quote_id)
    return jsonify(quote), 200


@app.route(rule='/quote/add', methods=['GET', 'POST'])
def add_quote():
    quote_to_add = request.args['quote']
    crud_ops.add_quote(quote=quote_to_add)
    response = {"message": "Quote was added successfully", "status_code": 201}
    return jsonify(response), 201


@app.route(rule='/quote/delete', methods=['GET'])
def delete_quote():
    quote_id = request.args['_id']
    crud_ops.delete_quote(quote_id=quote_id)
    response = {"message": "Quote was deleted successfully", "status_code": 200}
    return jsonify(response), 200


@app.route(rule='/quote/update_rating', methods=['GET'])
def update_quote_rating():
    quote_id = request.args['_id']
    new_rating = float(request.args['new_rating'])
    crud_ops.update_quote_rating(quote_id=quote_id,
                                 new_rating=new_rating)
    response = {"message": "Quote rating was updated successfully", "status_code": 200}
    return jsonify(response), 200


@app.route(rule='/quotes/similar_quotes', methods=['GET'])
def get_similar_quotes():
    quote = request.args['quote']
    top = int(request.args['top'])
    similar_quotes = filters.get_similar_quotes(quote=quote, top=top)
    return jsonify(similar_quotes), 200


if __name__ == "__main__":
    app.run(debug=True)