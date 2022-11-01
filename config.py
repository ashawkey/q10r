import os

DEBUG = True

curdir = os.path.abspath(os.path.dirname(__file__))

QUESTIONNAIRE_DIR = os.path.join(curdir, 'questionnaires')
QUESTIONNAIRE_SUBMISSIONS_DIR = os.path.join(curdir, 'submissions')

# admin account to check the results and available questionnaires.
QUESTIONNAIRE_BASIC_AUTH = ('kiui', 'tmp_1123 j')

QUESTIONNAIRE_DEFAULTS = {
    "submit": "Submit",
    "messages": {
        "error": {
            "required": "Field is required"
        },
        "success": "Thank you! Your form has been submitted!"
    }
}

