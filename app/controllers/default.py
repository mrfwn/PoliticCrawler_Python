from flask import render_template , request,redirect, url_for
from app import app , db
#from app.models.tables import Gfo
from app.models.tables import DeputadoF,Gastos
from werkzeug import secure_filename
import os
from apscheduler.schedulers.background import BackgroundScheduler
from operator import itemgetter
import operator
import jinja2

sched = BackgroundScheduler() # Scheduler object
sched.start()

def job1():
   DeputadoF.getDeputados(DeputadoF)

def job2():
   Gastos.getGastos(Gastos)

sched.add_job(job1, 'interval', hours=48)
sched.add_job(job2, 'interval', hours=24)



@app.route("/index")
@app.route("/")
def index():  
    top10alimentacao = Gastos.top10Aleimentacao()
    top10alimentacao.sort(key=operator.itemgetter('Total'))
    top10combustivel = Gastos.top10Combustivel()
    top10combustivel.sort(key=operator.itemgetter('Total'))
    tamanhoAlimentacao = len(top10alimentacao)
    tamanhoCombustivel = len(top10combustivel)
    return render_template('dashboard.html',top10alimentacao=top10alimentacao,top10combustivel=top10combustivel,tamanhoCombustivel=tamanhoCombustivel,tamanhoAlimentacao=tamanhoAlimentacao)

"""
@app.route("/upload")
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('GFO - Relatorio Detalhado.xlsx')))
      Gfo.loadPlanilha()
   return redirect(url_for('index'))
"""