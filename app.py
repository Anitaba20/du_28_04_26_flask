from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)
@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route('/knihy', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/knihy/<int:id>', methods=['GET'])
def get_book(id):


# TODO DOPLNIT
@app.route('/knihy', methods=['POST'])
def add_book():
    print(request.json)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Zobrazenie jednej knihy:
@app.route('/knihy/<int:id>', methods=['GET'])
def zobraz_knihu(id):
    for kniha in knihy:
        if kniha["id"] == id:
            return jsonify(kniha)

    return jsonify({"chyba": "Kniha nenájdená"}), 404










if __name__ == '__main__':
    app.run()