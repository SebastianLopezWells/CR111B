from flask import(
    Flask,
    request
)

from app.database import notes

app = Flask(__name__)

@app.get("/notes")
def index():
    out = notes.scan()
    return out


@app.get("/notes/<int:pk>")
def integers(pk):
    out = notes.select_by_number(pk)
    return out


@app.post("/notes")
def create_notes():
    dt_body = request.json
    notes.create(dt_body)

    return "", 204

@app.put("/notes/<int:pk>")
def update_notes(pk):
    dt_body = request.json
    notes.update(dt_body, pk)

    return "", 204

@app.delete("/notes/<int:pk>")
def delete_notes(pk):
    notes.delete(pk)
    
    return "", 204