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

# -------------------------------
# Zobrazenie jednej knihy:
@app.route('/knihy/<int:id>', methods=['GET'])
def get_one_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404


# Aktualizácia knihy:
@app.route('/knihy/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book["id"] == id:
            book["title"] = request.json["title"]
            book["author"] = request.json["author"]
            return jsonify(book)

    return {"error": "Book not found"}, 404


# Vymazanie knihy:
@app.route('/knihy/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": "Book deleted"}

    return {"error": "Book not found"}, 404


if __name__ == '__main__':
    app.run()


