from mysql import connector

class Model:
    """
    *******************************************
    * A data model with MySQL for a agenda DB *
    *******************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor(buffered=True)
    
    def close_db(self):
        self.cnx.close()
    
    """
    ********************
    * contacto methods *
    ********************
    """
    def create_contacto(self,contacto,nombre,apPaterno,apMaterno,correo,telefono):
        try:
            sql = 'INSERT INTO contacto (`id_contacto`, `nombre`,`apellido_paterno`,`apellido_materno`,`correo`,`telefono`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (contacto,nombre,apPaterno,apMaterno,correo,telefono)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    def read_a_contacto(self,contacto):
        try:
            sql = 'SELECT * FROM contacto WHERE id_contacto = %s'
            vals = (contacto,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err
    
    def read_all_contactos(self):
        try:
            sql = 'SELECT * FROM contacto'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def update_contacto(self,fields,vals):
        '''fields = []
        vals = []
        if nombre != '':
            vals.append(nombre)
            fields.append('nombre = %s')
        if apPaterno != '':
            vals.append(apPaterno)
            fields.append('apellido_paterno = %s')
        if apMaterno != '':
            vals.append(apMaterno)
            fields.append('apellido_materno = %s')
        if correo != '':
            vals.append(correo)
            fields.append('correo = %s')
        if telefono != '':
            vals.append(telefono)
            fields.append('telefono = %s')
        vals.append(contacto)
        vals = tuple(vals)'''


        try:
            sql = 'UPDATE contacto SET '+','.join(fields) + 'WHERE id_contacto = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_contacto(self,contacto):
        try:
            sql = 'DELETE FROM contacto WHERE id_contacto = %s'
            vals = (contacto,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    ***************
    * cita methods *
    ***************
    """

    def create_cita(self,fecha,asunto,ubicacion,id_contacto):
        try:
            sql = 'INSERT INTO cita (`fecha`,`asunto`,`ubicacion`,`id_contacto`) VALUES (%s,%s,%s,%s)'
            vals = (fecha,asunto,ubicacion,id_contacto)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_cita(self,id_cita):
        try:
            #sql = 'SELECT cita.*, contacto.* FROM cita  JOIN contacto ON contacto.id_contacto = cita.id_contacto and cita.id_cita =  %s'
            sql = "SELECT id_cita,fecha, asunto, ubicacion, CONCAT(contacto.nombre ,%s,contacto.apellido_paterno,%s, contacto.apellido_materno) FROM cita JOIN contacto ON contacto.id_contacto = cita.id_contacto and cita.id_cita =  %s"
            #sql = 'SELECT c.id_cita,c.fecha, c.asunto, c.ubicacion,contacto.nombre ,contacto.apellido_paterno,contacto.apellido_materno FROM cita c, contacto where contacto.id_contacto = c.id_contacto and and c.id_cita =  %s'
            vals = (' ',' ',id_cita,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err
    
    def read_all_citas(self):
        try:
            #sql = 'SELECT c.id_cita,c.fecha,c.asunto,c.ubicacion,CONCAT(contacto.nombre ,' ',contacto.apellido_paterno,' ', contacto.apellido_materno) AS contactonombre FROM cita c,contacto where c.id_contacto = contacto.id_contacto'
            #sql = 'SELECT id_cita,fecha, asunto, ubicacion, CONCAT(contacto.nombre ,' ',contacto.apellido_paterno,' ', contacto.apellido_materno) FROM cita JOIN contacto ON contacto.id_contacto = cita.id_contacto'
            #sql = 'SELECT * FROM cita'
            #sql = 'SELECT id_cita,fecha, asunto, ubicacion, CONCAT(contacto.nombre,' ',contacto.apellido_paterno,' ',contacto.apellido_materno) FROM cita, contacto'
            sql = 'SELECT c.id_cita,c.fecha, c.asunto, c.ubicacion, CONCAT(contacto.nombre ,%s,contacto.apellido_paterno,%s,contacto.apellido_materno) as nombrecontacto FROM cita c, contacto where contacto.id_contacto = c.id_contacto'
            #sql = 'SELECT c.id_cita,c.fecha, c.asunto, c.ubicacion,contacto.nombre ,contacto.apellido_paterno,contacto.apellido_materno FROM cita c, contacto where contacto.id_contacto = c.id_contacto'
            vals = (' ', ' ')
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def update_cita(self,fields,vals):
        try:
            sql = 'UPDATE cita SET '+','.join(fields) + 'WHERE id_cita = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_cita(self,id_cita):
        try:
            sql = 'DELETE FROM cita WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_all_citas_from_contacto(self,id_contacto):
        try:
            #sql = 'SELECT * FROM cita WHERE id_contacto = %s'
            sql = 'SELECT c.id_cita,c.fecha, c.asunto, c.ubicacion, CONCAT(contacto.nombre ,%s,contacto.apellido_paterno,%s,contacto.apellido_materno) as nombrecontacto FROM cita c, contacto where contacto.id_contacto = c.id_contacto and contacto.id_contacto = %s'
            vals = (' ',' ',id_contacto,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    
