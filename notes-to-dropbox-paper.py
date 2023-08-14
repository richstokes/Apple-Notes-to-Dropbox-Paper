import os
import sys
import dropbox
import time
from dropbox.exceptions import ApiError, AuthError
from dropbox.paper import ImportFormat
from macnotesapp import NotesApp

TIMESTAMP = time.strftime("%Y_%m_%d-%H-%M-%S")
notesapp = NotesApp()
notes = notesapp.notes(accounts=["iCloud"])  # , "On My Mac"])

try:
    TOKEN = os.environ["paperApiKey"]
except:
    TOKEN = ""
    if not TOKEN:
        print(
            "Create token here: https://dropbox.tech/developers/generate-an-access-token-for-your-own-account"
        )
        print("Then set env var with something like `export paperApiKey=foobar123`")
        sys.exit("Print API Key not set in env var `paperApiKey`, exiting...")

print("Creating a Dropbox object...")
with dropbox.Dropbox(TOKEN) as dbx:
    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an "
            "access token from the app console on the web."
        )

    # Create a backup folder
    try:
        print(f"Creating Apple Notes backup folder ({TIMESTAMP})...")
        folder_id = dbx.paper_folders_create(f"Apple Notes {TIMESTAMP}").folder_id

    except ApiError as err:
        sys.exit(err)

    # Copy all apple notes into dropbox paper as HTML
    for note in notes:
        print(f"Backing up {note.name} to Dropbox Paper..")

        # Convert string to bytes
        try:
            note_bytes = note.body.encode("utf-8")
            dbx.paper_docs_create(note_bytes, ImportFormat.html, folder_id)
        except Exception as e:
            print(f"Error backing up {note.name}: {e}")
            # quit("early exit due to error")

        # quit("early exit")
