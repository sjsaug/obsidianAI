## About
An Ollama-based RAG app to interact with your Obsidian.md notes.

## Setup
1. Download, install and run the Ollama app (https://ollama.com/download)
2. Run 'ollama pull llama3.1' (if you'd like to use a different model, pull your desired model and edit the MODEL variable in main.py)
3. pip install -r requirements.txt (please note this may become outdated with time)
4. Set your notes directory in NOTES_PATH (or drop some notes in the 'data' directory)
5. Run main.py

## Common Fixes
- If you are receiving port-related errors, make sure the Ollama app is running. I have it configured to run at startup.
- Ensure your notes are .md files. To get this working with PDF or other file types you will need to edit the load_docs() function. I also haven't tested this with directories containing sub-directories.