import os
from flask import Flask, jsonify,  render_template, request, redirect, url_for, send_from_directory, redirect
from werkzeug import secure_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Herramienta, Proyecto
from archivo import crear
import subprocess
app = Flask(__name__)
 

engine = create_engine('sqlite:///lista_herramienta.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/herramientas/menu/JSON')
def listaHerramientaJSON():
	items = session.query(Herramienta).all()
	return jsonify(Herramienta=[i.serialize for i in items])

@app.route('/herramientas/new/', methods=['GET', 'POST'])
def newHerraminta():
    if request.method == 'POST':
        newItem = Herramienta(
            nombre=request.json['nombre'],  descripcion=request.json['descripcion'], parametros=request.json['parametros'])
        session.add(newItem)
        session.commit()
        return jsonify(Herramienta=newItem.serialize)
    
    
@app.route('/herramientas/<int:menu_id>/edit',methods=['GET', 'POST'])
def editMenuItem(menu_id):
    editedItem = session.query(Herramienta).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.json['nombre']:
            editedItem.nombre = request.json['nombre']
        if request.json['descripcion']:
            editedItem.descripcion = request.json['descripcion']
        if request.json['parametros']:
            editedItem.parametros = request.json['parametros']
        session.add(editedItem)
        session.commit()
        return jsonify(Herramienta=editedItem.serialize)
    
@app.route('/herramientas/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteMenuItem(menu_id):
    itemToDelete = session.query(Herramienta).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return jsonify({'response': "herramienta eliminada"})
        
@app.route('/proyectos/menu/JSON')
def listaProyectoJSON():
	items = session.query(Proyecto).all()
	return jsonify(Proyecto=[i.serialize for i in items])

@app.route('/proyectos/new/', methods=['GET', 'POST'])
def newProyecto():
    if request.method == 'POST':
        newItem = Proyecto(
            nombre=request.json['nombre'],  descripcion=request.json['descripcion'])
        session.add(newItem)
        session.commit()
        return jsonify(Proyecto=newItem.serialize)    
    
@app.route('/proyectos/<int:menu_id>/edit',methods=['GET', 'POST'])
def editproyect(menu_id):
    editedItem = session.query(Proyecto).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.json['nombre']:
            editedItem.nombre = request.json['nombre']
        if request.json['descripcion']:
            editedItem.descripcion = request.json['descripcion']
        session.add(editedItem)
        session.commit()
        return jsonify(Proyecto=editedItem.serialize)
 
@app.route('/proyectos/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteproyecto(menu_id):
    itemToDelete = session.query(Proyecto).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return jsonify({'response': "proyecto eliminada"})
    
@app.route('/')
@app.route('/hello')
def HelloWorld():

    items = session.query(Herramienta).all()

    output = ""

    for i in items:
        output += i.nombre
        output += i.descripcion
        output += i.parametros
        output += '</br>'

    return output

@app.route('/helloP')
def HelloP():

    items = session.query(Proyecto).all()

    output = ""

    for i in items:
        output += i.nombre
        output += i.descripcion
        output += '</br>'

    return output

@app.route('/condor/estado')
def estado():
    cmd = ["condor_status"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    return jsonify({"estado": out})

@app.route('/condor/cola')
def cola():
    cmd = ["condor_q"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    return jsonify({"cola": out})

app.config['UPLOAD_FOLDER'] = ''
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py','cpp'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/condor/file')
def student():
   return render_template("formulario.html")


@app.route('/upload', methods=['GET','POST'])
def upload():
    # Get the name of the uploaded file

    if request.method=='POST':
	file = request.files['file']
        print type(file)
	# Check if the file is one of the allowed types/extensions
	if file and allowed_file(file.filename):
		# Make the filename safe, remove unsupported chars
		filename = secure_filename(file.filename)
		# Move the file form the temporal folder to
		# the upload folder we setup
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		# Redirect the user to the uploaded_file route, which
		# will basicaly show on the browser the uploaded file
		return jsonify({"file": filename})
    return render_template("upload.html")
  
  

@app.route('/condor/crear',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      executable = request.form['executable']
      universe = request.form['universe']
      log = request.form['log']
      output = request.form['output']
      crear(executable, universe, log, output)

      return render_template("result.html",executable = executable,universe=universe, log=log, output=output)

@app.route('/condor/ejecucion/')
def ejecucion():
    cmd = ["condor_submit","foot.submit"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    
    return jsonify({"ejecucion": out})

@app.route('/condor/salida/')
def salida():
    file=open("ejecucion.out","r")
    file_r=file.read()
    json = jsonify({"salida": file_r})


    return render_template("result.html", json=json)


@app.route('/condor/log/')
def log():
    file = open("ejecucion.log", "r")
    file_r = file.read()

    return jsonify({"log": file_r})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
