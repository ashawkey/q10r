# q10r

This is a fork of [q10r](https://github.com/vlevit/q10r) modified to support embedding videos.

> q10r is a simple questionnaire web app based on Flask. 
It produces questionnaires from JSON files and stores submissions in JSON files under different directory. 
q10r also provides a page for viewing questionnaire results.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Make a questionnaire

Create a JSON file under `questionnaires`, follow the `example.json` to config your questionnaire.

### Deploy

```bash
# debug mode in local environment
python app.py --port=5000

# serve with waitress
waitress-serve --threads=32 --port=5000 app:app
```

The hosted pages:
* All available questionnaires, admin login required (http://localhost:5000)
* Questionnaire, publicly available (http://localhost:5000/example)
* Results, admin login required (http://localhost:5000/example/results)