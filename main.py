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
    print("Notes:")
    for i, note in enumerate(notes):
        print(f"{i}: Title: {note['title']}, Text: {note['text']}")
    index = int(input("inhalt der zu löschenden Notiz: "))
    if 0 <= index < len(notes):
        notes.pop(index)

def update_note():
    title = input("Titel der Notiz, die du aktualisieren willst: ")
    for note in notes:
        if note['title'] == title:
            note['text'] = input("Neuer Text: ")
            print("Notiz wurde aktualisiert.")
            return
    print("Keine Notiz mit diesem Titel gefunden.")

add_note()
delete_note()
update_note()
show_notes()