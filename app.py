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
            nombre=request.form['nombre'],  descripcion=request.form['descripcion'], parametros=request.form['parametros'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('HelloWorld'))
    else:
        return render_template('newmenuitem.html')
    
    
@app.route('/herramientas/<int:menu_id>/edit',methods=['GET', 'POST'])
def editMenuItem(menu_id):
    editedItem = session.query(Herramienta).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['nombre']:
            editedItem.nombre = request.form['nombre']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('HelloWorld'))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template('editmenuitem.html',item=editedItem)
    
@app.route('/herramientas/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteMenuItem(menu_id):
    itemToDelete = session.query(Herramienta).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('HelloWorld'))
    else:
        return render_template('deleteconfirmation.html', item=itemToDelete)

@app.route('/proyectos/menu/JSON')
def listaProyectoJSON():
	items = session.query(Proyecto).all()
	return jsonify(Proyecto=[i.serialize for i in items])

@app.route('/proyectos/new/', methods=['GET', 'POST'])
def newProyecto():
    if request.method == 'POST':
        newItem = Proyecto(
            nombre=request.form['nombre'],  descripcion=request.form['descripcion'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('HelloP'))
    else:
        return render_template('newproject.html')
    
    
@app.route('/proyectos/<int:menu_id>/edit',methods=['GET', 'POST'])
def editproyect(menu_id):
    editedItem = session.query(Proyecto).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['nombre']:
            editedItem.nombre = request.form['nombre']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('HelloP'))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template('editproject.html',item=editedItem)
    
@app.route('/proyectos/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteproyecto(menu_id):
    itemToDelete = session.query(Proyecto).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('HelloP'))
    else:
        return render_template('deleteproject.html', item=itemToDelete)

    
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
    return out

@app.route('/condor/cola')
def cola():
    cmd = ["condor_q"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    return out

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

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def uploader():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)



@app.route('/condor/crear',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      executable = request.form['executable']
      universe = request.form['universe']
      inputt = request.form['input']
      output = request.form['output']
      crear(executable, universe, inputt, output)

      return render_template("result.html",executable = executable,universe=universe, inputt=inputt, output=output)

@app.route('/condor/ejecucion/')
def ejecucion():
    cmd = ["condor_submit","foot.submit"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    return out


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
