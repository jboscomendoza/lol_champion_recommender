import recommender as rec
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from forms import ChooseForm, StatForm
from markupsafe import escape


app = Flask(__name__)
app.config['SECRET_KEY'] = '7283hjbdscfzc78sdm3l3s8sbh23bds890fasdfz21p'


LISTA_CHAMPS = rec.CHAMP_NAMES


@app.route("/recomendaciones/<string:campeon>/", methods=("GET", "POST"))
def link_me(campeon):
    form = ChooseForm()
    form_stat = StatForm()

    if form.validate_on_submit():
        campeon = form.choose_champ.data
        return redirect(url_for("link_me", campeon=campeon))
    recomendaciones = rec.recoms(campeon, cuantos=12)
    
    stats = rec.get_stats(campeon)
    return render_template(
        "recomendaciones.html",
        campeon=campeon,
        recomendaciones=recomendaciones,
        stats=stats,
        get_role=rec.get_role,
        form=form,
        form_stat=form_stat
    )


@app.route("/", methods=("GET", "POST"))
@app.route("/home/", methods=("GET", "POST"))
def mostrar_forma():
    form = ChooseForm()
    form_stat = StatForm()

    if form.validate_on_submit():
        campeon = form.choose_champ.data
        return redirect(url_for("link_me", campeon=campeon))
    
    return render_template("home.html", form = form, form_stat=form_stat)


if __name__ == "__main__":
    app.run()