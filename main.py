notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]

def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")

def add_note():
    title = input("Title: ")
    text = input("Text: ")
    notes.append({"title": title, "text": text})

def delete_note():
    pass 

def update_note():
    pass

add_note()
# delete_note()
# update_note()
show_notes()