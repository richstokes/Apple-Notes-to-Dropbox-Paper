# Apple-Notes-to-Dropbox-Paper
Quick n' dirty script which backs up (copies) your Apple Notes to Dropbox Paper. Must be run on a Mac with access to your notes.  
&nbsp;

## How it works
- [This](https://github.com/RhetTbull/macnotesapp) really helpful python lib extracts the notes' HTML using Applescript
- The code in this repo creates a new, datestamped folder in your Dropbox Paper account
- Each note is copied to Dropbox Paper
- Unlock your Apple notes first to include locked ones

&nbsp;

## Setup & Run
1. `pip install -r requirements.txt`  
1. Create a new [Dropbox app with a generated token](https://dropbox.tech/developers/generate-an-access-token-for-your-own-account)
1. Export the token like: `export paperApiKey="foobar123"`
1. Run `python3 notes-to-dropbox-paper.py`