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


@app.route("/custom/", methods=("GET", "POST"))
def mostrar_custom():
    # str a dict
    stat = eval(request.args["stat"])
    return(render_template("custom.html", stat=stat ))


@app.route("/", methods=("GET", "POST"))
@app.route("/home/", methods=("GET", "POST"))
def mostrar_forma():
    form = ChooseForm()
    form_stat = StatForm()

    if form.validate_on_submit() and form.submit:
        campeon = form.choose_champ.data
        return redirect(url_for("link_me", campeon=campeon))
    elif form_stat.validate_on_submit() and form_stat.submit_stat:
        stat = request.form.to_dict()
        for i in ["csrf_token", "submit_stat"]:
            stat.pop(i)
        return redirect(url_for("mostrar_custom", stat=stat))

    return render_template("home.html", form = form, form_stat=form_stat)


if __name__ == "__main__":
    app.run()