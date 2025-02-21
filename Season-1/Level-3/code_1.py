# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

"""
1ère réflexion à vue d'oeil avant de regarder les autres parties du code:
- Je pense que self.password (et peut-être même self.username) devraient être déclarés comme ceci,
  self.__password et self.__username afin d'être privé (et accessible via des méthodes spécifiques)
"""

class TaxPayer:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass

        # defends against path traversal attacks
        """
        Pour le premier hack test_1, il suffit de tester '.' au lieu de '..' car il n'y a pas de raisons
        pour que le nom du chemin commence par un point.
        """
        if path.startswith('/') or path.startswith('.'):
            return None

        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")
        
        # Tests 2 de hack
        """
        On décortique la chaîne pour récupérer la partie saisie par l'utilisateur,
        et on effectue les tests sur celle-ci.
        """
        specified_path = path.replace(os.path.dirname(os.path.abspath(__file__)) + '/', '')

        if specified_path.startswith('/') or specified_path.startswith('.'):
           return None
        #

        try:
            with open(path, 'rb') as form:
                tax_data = bytearray(form.read())
        except:
            print("Unable to open the specified path")

        # assume that tax data is returned on screen after this
        return path

