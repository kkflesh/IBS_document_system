from flask import Blueprint, render_template
from flaskblog.document.forms import UpdateISO

document = Blueprint('document', __name__)


@document.route("/ISO")
def ISO():
    form = UpdateISO()
    return render_template("document/ISO.html", title="ISO", form =form)