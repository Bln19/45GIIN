#importar modulos
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from mysql.connector import Error as MySQLError
import os
import database as db
from flask_cors import CORS
import logging
import qrcode


logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

# Configuración básica del logger: escribe en consola y establece el nivel mínimo a DEBUG
logging.basicConfig(level=logging.DEBUG)


#acceder al archivo index.html
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#unir src templates a la carpeta del proyecto
template_dir = os.path.join(template_dir, 'src', 'templates')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
QR_FOLDER = os.path.join(BASE_DIR, 'qrfolder')

#inicializar flask
app = Flask(__name__, template_folder = template_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['QR_FOLDER'] = QR_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 48 * 1024 * 1024
CORS(app)


#--------------------------------------------------------------------------------------------------------------------------------#
#RUTAS DE LA APLICACIÓN
#--------------------------------------------------------------------------------------------------------------------------------#

#ruta principal - VER EMPRESA
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM empresa")
    myresult = cursor.fetchall()
    #Convertir datos a diccionario
    empresaData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        empresaData.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', empresaData=empresaData)

@app.route('/empresa', methods=['GET'])
def getEmpresa():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM empresa")
    myresult = cursor.fetchall()
    #Convertir datos a diccionario
    empresaData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        empresaData.append(dict(zip(columnNames, record)))
    cursor.close()
    return jsonify(empresaData)



@app.route('/empresa', methods=['POST'])
def addEmpresa():
    data = request.json
    nombre = data['nombre']
    direccion = data['direccion']
    cif = data['cif']
    email = data['email']
    telefono = data['telefono']
    
    if nombre and direccion and cif and email and telefono:
        cursor = db.database.cursor()
        sql = "INSERT INTO empresa (nombre, direccion, cif, email, telefono) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, direccion, cif, email, telefono))
        db.database.commit()
        return jsonify("Empresa añadida")
    else:
        return jsonify("Datos incompletos"), 400



@app.route('/empresa/<id_empresa>', methods=['DELETE'])
def deleteEmpresa(id_empresa):
    try: 
        cursor = db.database.cursor()
        sql = "DELETE FROM empresa WHERE id_empresa = %s"
        cursor.execute(sql, (id_empresa,))
        db.database.commit()

        if cursor.rowcount == 0:
            return jsonify("Empresa no encontrada"), 404

        return jsonify("Empresa eliminada")
    except Exception as e:
        return jsonify(str(e)), 500


@app.route('/edit_empresa/<id_empresa>', methods=['GET'])
def editEmpresa(id_empresa):
    logging.info('Entra en EDIT Empresa')
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM empresa WHERE id_empresa = %s", (id_empresa,))

    # Obtiene los resultados de la consulta
    myresult = cursor.fetchall()
    db.database.commit()

    empresaData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        empresaData.append(dict(zip(columnNames, record)))
        logging.info(empresaData)
    cursor.close()
    return jsonify(empresaData)


@app.route('/update_empresa/<id_empresa>', methods=['POST'])
def updateEmpresa(id_empresa):
    try:

        data = request.get_json()
        nombre = data['nombre']
        direccion = data['direccion']
        cif = data['cif']
        email = data['email']
        telefono = data['telefono']

  
        cursor = db.database.cursor()
        query = """
        UPDATE empresa 
        SET nombre = %s, direccion = %s, cif = %s, email = %s, telefono = %s 
        WHERE id_empresa = %s
        """
        cursor.execute(query, (nombre, direccion, cif, email, telefono, id_empresa))

        db.database.commit()
        cursor.close()

        return jsonify({'message': 'Empresa actualizada con éxito'}), 200

    except Exception as e:
        print(e)
        return jsonify({'message': 'Error al actualizar la empresa'}), 500




#--------------------------------------------------------------------------------------------------------------------------------#

######      PROVEEDORES     #########

#--------------------------------------------------------------------------------------------------------------------------------#
#Ruta para VER PROVEEDORES

@app.route('/proveedores', methods=['GET'])
def getProveedor():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM proveedor")
    myresult = cursor.fetchall()
    #Convertir datos a diccionario
    proveedorData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        proveedorData.append(dict(zip(columnNames, record)))
    cursor.close()
    return jsonify(proveedorData)

#Ruta para AÑADIR  PROVEEDOR en la BD

@app.route('/add_proveedor', methods=['POST'])
def add_proveedor():
    data = request.json
    nombre = data['nombre']
    cif = data['cif']
    direccion = data['direccion']
    telefono = data['telefono']
    email = data['email']
    
    if nombre and cif and direccion and telefono and email:
        id_proveedor = insert_proveedor(nombre, cif, direccion, telefono, email)
        if id_proveedor:
            return jsonify("Proveedor añadido")
        else:
            return jsonify("Error al añadir proveedor")
    else:
        return jsonify("Datos incompletos"), 400
    

#FUNCION AUXILIAR para INSERTAR PROVEEDOR en la BD
def insert_proveedor(nombre, cif, direccion, telefono, email):
    try:
        cursor= db.database.cursor()
        sql = "INSERT INTO proveedor (nombre, cif, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, cif, direccion, telefono, email))
        db.database.commit()
        logging.info(cursor.lastrowid)
        return cursor.lastrowid  # Retorna el ID del proveedor insertado
    except Exception as e:
         logging.error("Error al insertar el código QR: %s", str(e))


#Ruta para ELIMINAR PROVEEDOR de la BD
         
@app.route('/delete_proveedor/<string:id>', methods=['DELETE'])
def delete_proveedor(id):
    try:
        cursor = db.database.cursor()

        #Eliminar las entradas en la tabla intermedia producto_proveedor que tienen el id del proveedor a eliminar
        sql_delete_related = "DELETE FROM producto_proveedor WHERE id_proveedor=%s"
        cursor.execute(sql_delete_related, (id,))

        # Eliminar los productos que ya no están referenciados y que pertenecen al proveedor a eliminar
        sql_delete_productos = "DELETE FROM producto WHERE id_producto NOT IN (SELECT id_producto FROM producto_proveedor)"
        cursor.execute(sql_delete_productos)

        #Eliminar el proveedor
        sql_delete_proveedor = "DELETE FROM proveedor WHERE id_proveedor=%s"
        cursor.execute(sql_delete_proveedor, (id,))
        
        db.database.commit()
        cursor.close()
        return jsonify({"success": True, "message": "Proveedor y productos relacionados eliminados correctamente"})
    except Exception as e:
        db.database.rollback()  # importante para deshacer los cambios si algo sale mal
        cursor.close()
        return jsonify({"success": False, "message": str(e)})

    

@app.route('/edit_proveedor/<id_proveedor>', methods=['GET'])
def editProveedor(id_proveedor):
    logging.info('Entra en EDIT Proveedor')
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))

    # Obtiene los resultados de la consulta
    myresult = cursor.fetchall()
    db.database.commit()

    proveedorData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        proveedorData.append(dict(zip(columnNames, record)))
        logging.info(proveedorData)
    cursor.close()
    return jsonify(proveedorData)


@app.route('/update_proveedor/<id_proveedor>', methods=['POST'])
def updateProveedor(id_proveedor):
    try:
        # Obtén los datos enviados desde el frontend
        data = request.get_json()
        nombre = data['nombre']
        cif = data['cif']
        direccion = data['direccion']
        telefono = data['telefono']
        email = data['email']

        # Crea una conexión a la base de datos y un cursor
        cursor = db.database.cursor()

        # Escribe la consulta SQL para actualizar los datos
        query = """
        UPDATE proveedor 
        SET nombre = %s, cif = %s, direccion = %s, telefono = %s,  email = %s  
        WHERE id_proveedor = %s
        """
        cursor.execute(query, (nombre, cif, direccion, telefono, email, id_proveedor))

        # Aplica los cambios en la base de datos
        db.database.commit()
        cursor.close()

        return jsonify({'message': 'Proveedor actualizado con éxito'}), 200

    except Exception as e:
        print(e)
        return jsonify({'message': 'Error al actualizar el proveedor'}), 500




#--------------------------------------------------------------------------------------------------------------------------------#

######      PRODUCTO     #########

#--------------------------------------------------------------------------------------------------------------------------------#

#Ruta para VER PRODUCTOS

@app.route('/productos', methods=['GET'])
def getProductos():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM producto")
    myresult = cursor.fetchall()
    #Convertir datos a diccionario
    productoData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        productoData.append(dict(zip(columnNames, record)))
    cursor.close()
    return jsonify(productoData)



#RUTA PARA VER DETALLE UN PRODUCTO

@app.route('/producto_detalle/<id_producto>', methods=['GET'])
def getProducto(id_producto):
    try:
        cursor = db.database.cursor()

        # Obtener detalles del producto
        cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
        producto_result = cursor.fetchall()

        productoData = []
        columnNames = [column[0] for column in cursor.description]
        for record in producto_result:
            productoData.append(dict(zip(columnNames, record)))

        if productoData:
            id_codigoqr = productoData[0].get('id_codigoqr')
            logging.info("DENTRO DE PRODUCTO DATA")
            logging.info(id_codigoqr)

            # Obtener imagen del código QR si existe
            if id_codigoqr:
                cursor.execute("SELECT imagen FROM codigo_qr WHERE id_codigoqr = %s", (id_codigoqr,))
                qr_result = cursor.fetchone()
                logging.info("QR RESULT")
                logging.info(qr_result)

                if qr_result:
                    imagen_path_qr = qr_result[0]
                    logging.info("IMAGEN PATH")
                    logging.info(imagen_path_qr)
                    if imagen_path_qr != '':
                        productoData[0]['imagenCodigoQR'] = imagen_path_qr
                    else:
                        productoData[0]['imagenCodigoQR'] = 'Imagen QR no encontrada'
            
            # Obtener el stock del producto
            cursor.execute("SELECT stock FROM inventario_producto WHERE id_producto = %s", (id_producto,))  
            stock_result = cursor.fetchone()
            logging.info("STOCK")
            logging.info(stock_result)
            stock = stock_result[0] if stock_result else 0
            if productoData:
                productoData[0]['stock'] = stock

            # Obtener el proveedor del producto
            cursor.execute("SELECT id_proveedor FROM producto_proveedor WHERE id_producto = %s", (id_producto,))
            id_proveedor_result = cursor.fetchone()
            id_proveedor = id_proveedor_result[0] if id_proveedor_result else None
            logging.info("ID_PROVEEDOR")
            logging.info(id_proveedor)
            
            if id_proveedor:
                 
                cursor.execute("SELECT id_proveedor, nombre, cif FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
                proveedor_result = cursor.fetchone()
                if proveedor_result:
                    productoData[0]['id_proveedor'] = proveedor_result[0]
                    productoData[0]['nombre_proveedor'] = proveedor_result[1]
                    productoData[0]['cif_proveedor'] = proveedor_result[2]
        
        cursor.close()
        return jsonify(productoData)

    except Exception as e:
        print(e)
        return jsonify({'message': 'Error al obtener los detalles del producto'}), 500


#Ruta para ELIMINAR PRODUCTO de la BD

@app.route('/delete_producto/<id_producto>', methods=['DELETE'])
def delete_producto(id_producto):
    try:
        cursor = db.database.cursor()

        #Eliminar el stock asociado a id_producto
        sql_delete_stock = "DELETE FROM inventario_producto WHERE id_producto=%s"
        cursor.execute(sql_delete_stock, (id_producto,))

        # Eliminar las entradas que pertenecen al producto en la tabla intermedia producto_proveedor
        sql_delete_related = "DELETE FROM producto_proveedor WHERE id_producto=%s"
        cursor.execute(sql_delete_related, (id_producto,))

        #Eliminar el producto
        sql = "DELETE FROM producto WHERE id_producto=%s"
        cursor.execute(sql, (id_producto,))
        
        db.database.commit()
        cursor.close()
        return jsonify({"success": True, "message": "Producto eliminado correctamente"}), 200
    except Exception as e:
        db.database.rollback()
        cursor.close()
        return jsonify({"success": False, "message": str(e)}), 500


#RUTA PARA CARGAR/SERVIR IMAGENES
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    logging.info(send_from_directory(app.config['UPLOAD_FOLDER'], filename))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#RUTA PARA CARGAR/SERVIR QT
    
@app.route('/qrfolder/<filename>')
def uploaded_qr(filename):
    return send_from_directory(app.config['QR_FOLDER'], filename)
   

#Ruta para AÑADIR PRODUCTO de la BD

@app.route('/add_producto', methods=['POST'])
def addProducto():
    logging.info(request)
    logging.info("Request files: %s", request.files)
    if 'imagen' not in request.files:
        return jsonify("No se encontró el archivo de imagen"), 400
    
    imagen = request.files.get('imagen')

    if imagen.filename == '':
        logging.info("No se seleccionó ningún archivo")
        return "No se seleccionó ningún archivo", 400

    if imagen and imagen.read() == b'':
        logging.info("El archivo de imagen está vacío")
        return "El archivo de imagen está vacío", 400
    imagen.seek(0)

    if imagen.filename == '':
        return jsonify("No se seleccionó ninguna imagen"), 400

    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        # Crea la carpeta si no existe
        os.makedirs(upload_folder)  
    if imagen:
        filename = secure_filename(imagen.filename)
        imagen_path = os.path.join(upload_folder, filename).replace("\\", "/")
        try:
            imagen.save(imagen_path)
            relative_imagen_path = os.path.join('uploads', filename).replace("\\", "/")
            logging.info(relative_imagen_path)
        except Exception as e:
                logging.error("No se ha guardado la imagen: %s", str(e))
                return jsonify(str(e)), 500

    data = request.form
    logging.info(data)

    referencia = data.get('referencia')
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    tamano = data.get('tamano')
    color = data.get('color')
    material = data.get('material')
    precio = data.get('precio')
    id_proveedor = data.get('id_proveedor')
    stock = data.get('stock')
    id_inventario_constante = 1


    if id_proveedor == 'nuevo' or not id_proveedor:
        nombre_proveedor = data.get('nombre_proveedor')
        cif_proveedor = data.get('cif_proveedor')
        direccion_proveedor = data.get('direccion_proveedor')
        telefono_proveedor = data.get('telefono_proveedor')
        email_proveedor = data.get('email_proveedor')
        try:
            id_proveedor = insert_proveedor(nombre_proveedor, cif_proveedor, direccion_proveedor, telefono_proveedor, email_proveedor)
        except Exception as e:
            logging.error("Error al insertar el código QR: %s", str(e))

    
    if referencia and nombre and descripcion and tamano and color and material and precio:
        try:
            cursor = db.database.cursor()
            qr_folder = app.config['QR_FOLDER']
            if not os.path.exists(qr_folder):
                os.makedirs(qr_folder)

            qr_filename = 'qr_code_' + referencia + '.png'
            qr_path = os.path.join(qr_folder, qr_filename).replace("\\", "/")
            relative_qr_path = os.path.join('qrfolder', qr_filename).replace("\\", "/")
            # Generar un nuevo código QR
            qr = qrcode.make(referencia) 
            qr.save(qr_path)

            try:
                # Ejecuta la inserción
                cursor.execute("INSERT INTO codigo_qr (codigo_qr, estado, imagen) VALUES (%s, %s, %s)", (referencia, True, relative_qr_path))
                db.database.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                id_codigoqr = cursor.fetchone()[0]
            except Exception as e:
                logging.error("Error al insertar el código QR: %s", str(e))
                return jsonify(str(e)), 500
        
            try:
                sql = ("INSERT INTO producto (id_codigoqr, referencia, nombre, descripcion, tamano, color, material, precio, imagen) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (id_codigoqr, referencia, nombre, descripcion, tamano, color, material, precio, relative_imagen_path))
                # Marcar el código QR como usado
                cursor.execute("UPDATE codigo_qr SET estado = True WHERE id_codigoqr = %s", (id_codigoqr,))
                db.database.commit()
                

                cursor.execute("SELECT LAST_INSERT_ID()")
                id_producto = cursor.fetchone()[0]

                if id_proveedor:
                    cursor.execute("INSERT INTO producto_proveedor (id_producto, id_proveedor) VALUES (%s, %s)", (id_producto, id_proveedor))
                    db.database.commit()
                
                cursor.execute("INSERT INTO inventario_producto (id_inventario, id_producto, stock) VALUES (%s, %s, %s)", (id_inventario_constante, id_producto, stock))
                db.database.commit()

                return jsonify("Producto añadido con éxito")
            
            except Exception as e:
                logging.error("Error al añadir el producto a la base de datos: %s", str(e))
                return jsonify(str(e)), 500

        except Exception as e:
            return jsonify(str(e)), 500
    else:
        return jsonify("Datos incompletos"), 400
    
    
#Ruta para EDITAR PRODUCTO de la BD

@app.route('/edit_producto/<id_producto>', methods=['GET'])
def editProducto(id_producto):
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))

    # Obtiene los resultados de la consulta
    myresult = cursor.fetchall()
    db.database.commit()

    productoData = []
    columnNames = [column [0] for column in cursor.description]
    for record in myresult:
        productoData.append(dict(zip(columnNames, record)))
    cursor.close()
    return jsonify(productoData)

@app.route('/update_producto/<id_producto>', methods=['POST'])
def updateProducto(id_producto):
    try:
        referencia = request.form.get('referencia')
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        tamano = request.form.get('tamano')
        color = request.form.get('color')
        material = request.form.get('material')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        imagen = request.files.get('imagen')
        imagen_actual=request.form.get('imagenActual')
        if imagen:
            upload_folder = app.config['UPLOAD_FOLDER']
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join(upload_folder, filename).replace("\\", "/")
            imagen.save(imagen_path)
            relative_imagen_path = os.path.join('uploads', filename).replace("\\", "/")
        else:
            # Omitir la actualización de la imagen
            relative_imagen_path = imagen_actual
            
        # Conexión a la base de datos y cursor
        cursor = db.database.cursor()
        id_inventario_constante = 1 
        # Consulta SQL para actualizar los datos
        query = """
        UPDATE producto
        SET referencia = %s, nombre = %s, descripcion = %s, tamano = %s, color = %s, material = %s, precio = %s, imagen = %s
        WHERE id_producto = %s
        """
        cursor.execute(query, (referencia, nombre, descripcion, tamano, color, material, precio, relative_imagen_path, id_producto))

        # Aplicar cambios en la base de datos
        db.database.commit()

        query_inventario = "UPDATE inventario_producto SET stock = %s WHERE id_producto = %s AND id_inventario = %s"
        cursor.execute(query_inventario, (stock, id_producto, id_inventario_constante))
        db.database.commit()
        cursor.close()

        return jsonify({'message': 'Producto actualizado con éxito'}), 200

    except Exception as e:
        print(e)
        return jsonify({'message': 'Error al actualizar el producto'}), 500
    

#Ruta para obtener STOCK de un PRODUCTO de la BD

@app.route('/get_stock_producto/<id_producto>', methods=['GET'])
def getStockProducto(id_producto):
    try:
        logging.info("ID PRODUCTO")
        logging.info(id_producto)
        cursor = db.database.cursor()
        id_inventario_constante = 1 
        cursor.execute("SELECT stock FROM inventario_producto WHERE id_producto = %s AND id_inventario = %s", (id_producto, id_inventario_constante))
        stock = cursor.fetchone()
        logging.info("STOCK")
        logging.info(stock)
        return jsonify({'stock': stock[0] if stock else 0}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error al obtener el stock del producto'}), 500
    
#--------------------------------------------------------------------------------------------------------------------------------#

# PEDIDO

#--------------------------------------------------------------------------------------------------------------------------------#


#RUTA PARA VER LISTADO de PEDIDOS
    
@app.route('/pedidos', methods=['GET'])
def getPedidos():
    cursor = db.database.cursor()
    cursor.execute("SELECT id_pedido, fecha, estado FROM pedido")
    myresult = cursor.fetchall()

    pedidosData = []
    columnNames = [column[0] for column in cursor.description]
    
    for record in myresult:
        pedido = dict(zip(columnNames, record))
        pedidosData.append(pedido)

    cursor.close()
    return jsonify(pedidosData)


#RUTA PARA VER DETALLE de UN PEDIDO

@app.route('/pedido_detalle/<id_pedido>', methods=['GET'])
def getPedido(id_pedido):
    cursor = db.database.cursor()
    query = """
    SELECT pp.id_pedido, ped.fecha, pp.id_producto, p.nombre as nombre_producto, 
    p.precio as precio_unitario, p.referencia, pp.cantidad,
    (p.precio * pp.cantidad) as precio_total
    FROM pedido_producto pp
    JOIN producto p ON pp.id_producto = p.id_producto
    JOIN pedido ped ON pp.id_pedido = ped.id_pedido
    WHERE pp.id_pedido = %s
    """
    cursor.execute(query, (id_pedido,))
    myresult = cursor.fetchall()
    logging.info("DETALLES PEDIDO")
    logging.info(myresult)
    # Convertir datos a diccionario
    pedidoData = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        pedidoData.append(dict(zip(columnNames, record)))
    cursor.close()
    return jsonify(pedidoData)


#RUTA PARA REALIZAR UN PEDIDO

@app.route('/add_pedido', methods=['POST'])
def add_pedido():
    try:
        data = request.json
        cursor = db.database.cursor()
        
        #Comprobar si hay suficiente stock para cada producto
        for producto in data['productos']:
            id_producto = producto['id_producto']
            cantidad_solicitada = producto['cantidad']

            cursor.execute("SELECT stock FROM inventario_producto WHERE id_producto = %s", (id_producto,))
            stock_result = cursor.fetchone()
            if not stock_result or stock_result[0] < cantidad_solicitada:
                return jsonify({"success": False, "message": "Stock insuficiente para el producto con ID: " + str(id_producto)}), 400
        #Crear entrada tabla pedido
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        estado = 0
        sql_pedido = "INSERT INTO pedido (fecha, estado) VALUES (%s, %s)"
        cursor.execute(sql_pedido, (fecha, estado))
        id_pedido = cursor.lastrowid

        #Añadir productos al pedido y actualizar stock
        for producto in data['productos']:
            id_producto = producto['id_producto']
            cantidad_solicitada = producto['cantidad']

            # Insertar en pedido_producto
            sql_pedido_producto = "INSERT INTO pedido_producto (id_pedido, id_producto, cantidad) VALUES (%s, %s, %s)"
            cursor.execute(sql_pedido_producto, (id_pedido, id_producto, cantidad_solicitada))

            # Actualizar stock en inventario_producto
            sql_update_stock = "UPDATE inventario_producto SET stock = GREATEST(0, stock - %s) WHERE id_producto = %s"
            cursor.execute(sql_update_stock, (cantidad_solicitada, id_producto))

        db.database.commit()
        return jsonify({"success": True, "message": "Pedido creado correctamente", "id_pedido": id_pedido})

    except Exception as e:
        db.database.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    

#Ruta para ELIMINAR PEDIDO de la BD

@app.route('/delete_pedido/<id_pedido>', methods=['DELETE'])
def delete_pedido(id_pedido):
    try:
        cursor = db.database.cursor()
        #Verificar el estado del pedido. Un pedido solo se puede eliminar si está pendiente de envio (estado = 0)
        cursor.execute("SELECT estado FROM pedido WHERE id_pedido=%s", (id_pedido,))
        estado = cursor.fetchone()
        if estado is None or estado[0] != 0:
            return jsonify({"success": False, "message": "Solo se pueden eliminar pedidos pendientes de enviar"}), 400

        #Obtener los productos y cantidades del pedido
        cursor.execute("SELECT id_producto, cantidad FROM pedido_producto WHERE id_pedido=%s", (id_pedido,))
        productos = cursor.fetchall()

        #Actualizar el stock de los productos
        for prod in productos:
            id_producto, cantidad = prod
            cursor.execute("UPDATE inventario_producto SET stock = stock + %s WHERE id_producto = %s", (cantidad, id_producto))

        # Eliminar las entradas en la tabla pedido_producto que tienen el id del pedido a eliminar
        sql_delete_pedido_producto = "DELETE FROM pedido_producto WHERE id_pedido=%s"
        cursor.execute(sql_delete_pedido_producto, (id_pedido,))

        # Eliminar el pedido
        sql_delete_pedido = "DELETE FROM pedido WHERE id_pedido=%s"
        cursor.execute(sql_delete_pedido, (id_pedido,))
        
        db.database.commit()
        cursor.close()
        return jsonify({"success": True, "message": "Pedido eliminado correctamente"}), 200
    except Exception as e:
        db.database.rollback()
        cursor.close()
        return jsonify({"success": False, "message": str(e)}), 500
    

#Ruta para EDITAR ESTADO de un PEDIDO de la BD   
    
@app.route('/update_estado_pedido/<id_pedido>', methods=['POST'])
def updateEstadoPedido(id_pedido):
    try:
        cursor = db.database.cursor()

        # Opcional: Verificar el estado actual del pedido
        cursor.execute("SELECT estado FROM pedido WHERE id_pedido=%s", (id_pedido,))
        estado_actual = cursor.fetchone()
        if estado_actual is None:
            return jsonify({"success": False, "message": "Pedido no encontrado"}), 404
        if estado_actual[0] != 0:
            return jsonify({"success": False, "message": "El pedido ya ha sido enviado o no puede ser actualizado"}), 400

        # Actualizar el estado del pedido a enviado (1)
        nuevo_estado = 1  # Estado enviado
        cursor.execute("UPDATE pedido SET estado=%s WHERE id_pedido=%s", (nuevo_estado, id_pedido))

        db.database.commit()
        cursor.close()
        return jsonify({"success": True, "message": "Estado del pedido actualizado a enviado"}), 200

    except Exception as e:
        db.database.rollback()
        cursor.close()
        return jsonify({"success": False, "message": str(e)}), 500


#--------------------------------------------------------------------------------------------------------------------------------#

# LANZAR APLICACION

#--------------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True, port=4000)