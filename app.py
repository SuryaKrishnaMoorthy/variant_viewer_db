from flask import Flask
app = Flask(__name__)
import vviewer.controllers.sources
import vviewer.controllers.samples
import vviewer.controllers.studies
import vviewer.controllers.bamFiles
