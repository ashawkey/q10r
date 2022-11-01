# q10r

This is a fork of [q10r](https://github.com/vlevit/q10r) modified to support embedding local videos.

> q10r is a simple questionnaire web app based on Flask. 
It produces questionnaires from JSON files and stores submissions in JSON files under different directory. 
q10r also provides a page for viewing questionnaire results.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Making a questionnaire

Create a JSON file under `questionnaires`, follow the `example.json` to config your questionnaire.

### Deploy

```bash
# debug mode in local environment
python app.py
```