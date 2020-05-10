from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    ********************************
    * A controller for a agenda DB *
    ********************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    """
    ***********************
    * General controllers *
    ***********************
    """

    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.citas_menu()
            elif o == '2':
                self.contactos_menu()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if (v != ""):
                fields.append(f+" = %s")
                vals.append(v)
        return fields,vals
    
    """
    ***********************
    * controllers for citas *
    ***********************
    """

    def citas_menu(self):
        o = '0'
        while o != '7':
            self.view.citas_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_cita()
            elif o == '2':
                self.read_cita()
            elif o == '3':
                self.read_all_citas()
            elif o == '4':
                self.update_cita()
            elif o == '5':
                self.delete_cita()
            elif o == '6':
                self.read_citas_where_contact()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_cita(self):
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Asunto: ')
        asunto = input()
        self.view.ask('Ubicacion: ')
        ubicacion = input()
        self.view.ask('id_contacto: ')
        id_contacto = input()
        return[fecha,asunto,ubicacion,id_contacto]



    def create_cita(self):
        fecha,asunto,ubicacion,id_contacto = self.ask_cita()
        out = self.model.create_cita(fecha,asunto,ubicacion,id_contacto)
        if out == True:
            self.view.ok("Cita" , "Agregada")
        else:
            #if out.errno == 1062:
                # self.view.error("El id de cita esta repedira") # No puede haber id de citas repetidas
             #   
            #else:
            self.view.error("No se pudo agregar la Cita, Revisar datos.") 
        return
    
    def read_cita(self):
        self.view.ask("id_cita: ")
        i_cita = input()
        cita = self.model.read_a_cita(i_cita)
        if type(cita) == tuple:
            self.view.show_cita_header(" Datos de la Cita " + i_cita+" ")
            self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            if cita == None:
                self.view.error("El id de la Cita no existe")
            else:
                self.view.error("Problema al leer el id de la Cita, Revisar datos")
        return
    
    def read_all_citas(self):
        citas = self.model.read_all_citas()
        if type(citas) == list:
            self.view.show_cita_header(" Todas las Citas ")
            for cita in citas:
                self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            print(citas)
            self.view.error("Problema al leer las Citas, Revisar")
        return

    def update_cita(self):
        self.view.ask("Cita a modificar: ")
        i_cita = input()
        cita = self.model.read_a_cita(i_cita)
        if type(cita) == tuple:
            self.view.show_cita_header(" Datos de la Cita "+i_cita+" ")
            self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            if cita == None:
                self.view.error("La Cita no exite en la bd")
            else:
                self.view.error("Problema al leer la Cita, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.ask_cita()
        fields, vals = self.update_lists(["fecha","asunto","ubicacion","id_contacto"],whole_vals)
        vals.append(i_cita)
        vals = tuple(vals)
        out = self.model.update_cita(fields,vals)
        if out == True:
            self.view.ok(i_cita, "Actualizada...")
        else:
            self.view.error("No se pudo actualizar la Cita, Revisa")
        return
    
    def delete_cita(self):
        self.view.ask("Cita a borrar: ")
        i_cita = input()
        count = self.model.delete_cita(i_cita)
        if count != 0:
            self.view.ok(i_cita,"Borro")
        else:
            if count == 0:
                self.view.error("La Cita no exite")
            else:
                self.view.error("Problema al borrar la Cita. Revisa")
        return
    
    def read_citas_where_contact(self):
        self.view.ask('id_contacto: ')
        id_contacto = input()
        citas = self.model.read_all_citas_from_contacto(id_contacto)
        if type(citas) == list:
            self.view.show_cita_header(" Todas las Citas del Contacto con id: "+id_contacto+" ")
            for cita in citas:
                self.view.show_a_cita(cita)
            self.view.show_cita_midder()
            self.view.show_cita_footer()
        else:
            self.view.error("Problema al leer las Citas, Revisar")
        return


    """
    *****************************
    * controllers for contactos *
    *****************************
    """
    def contactos_menu(self):
        o = '0'
        while o != '6':
            self.view.contactos_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_contacto()
            elif o == '2':
                self.read_contacto()
            elif o == '3':
                self.read_all_contactos()
            elif o == '4':
                self.update_contacto()
            elif o == '5':
                self.delete_contacto()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_contacto(self):
        self.view.ask('id_contacto: ')
        id_contacto = input()
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        apellido_paterno = input()
        self.view.ask('Apellido Materno: ')
        apellido_materno = input()
        self.view.ask('Correo: ')
        correo = input()
        self.view.ask('telefono: ')
        telefono = input()
        return [id_contacto,nombre,apellido_paterno,apellido_materno,correo,telefono]

    def create_contacto(self):
        id_contacto,nombre,apellido_paterno,apellido_materno,correo,telefono = self.ask_contacto()
        out = self.model.create_contacto(id_contacto,nombre,apellido_paterno,apellido_materno,correo,telefono)
        if out == True:
            self.view.ok("Contacto" , "Agregado")
        else:
            if out.errno == 1062:
                self.view.error("El id de Contacto esta repetido")
                
            else:
                self.view.error("No se pudo agregar el Contacto, Revisar datos.")
        return
    
    def read_contacto(self):
        self.view.ask("id_contacto: ")
        i_contacto = input()
        contacto = self.model.read_a_contacto(i_contacto)
        if type(contacto) == tuple:
            self.view.show_contacto_header(" Datos del Contacto " + i_contacto+" ")
            self.view.show_a_contacto(contacto)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            if contacto == None:
                self.view.error("El id del Contacto no existe")
            else:
                self.view.error("Problema al leer el id del Contacto, Revisar datos")
        return
    
    def read_all_contactos(self):
        contactos = self.model.read_all_contactos()
        if type(contactos) == list:
            self.view.show_contacto_header(" Todos los Contactos ")
            for contacto in contactos:
                self.view.show_a_contacto(contacto)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            self.view.error("Problema al leer los Contactos, Revisar")
        return
    
    def update_contacto(self):
        self.view.ask("Contacto a modificar: ")
        i_contacto = input()
        contacto = self.model.read_a_contacto(i_contacto)
        if type(contacto) == tuple:
            self.view.show_contacto_header(" Datos del Contacto "+i_contacto+" ")
            self.view.show_a_contacto(contacto)
            self.view.show_contacto_midder()
            self.view.show_contacto_footer()
        else:
            if contacto == None:
                self.view.error("El Contacto no exite en la bd")
            else:
                self.view.error("Problema al leer el Contacto, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.ask_contacto()
        fields, vals = self.update_lists(["id_contacto","nombre","apellido_paterno","apellido_materno","correo","telefono"],whole_vals)
        vals.append(i_contacto)
        vals = tuple(vals)
        out = self.model.update_contacto(fields,vals)
        if out == True:
            self.view.ok(i_contacto, "Actualizado...")
        else:
            self.view.error("No se pudo actualizar el Contacto, Revisa")
        return

    def delete_contacto(self):
        self.view.ask("Contacto a borrar: ")
        i_contacto = input()
        count = self.model.delete_contacto(i_contacto)
        if count != 0:
            self.view.ok(i_contacto,"Borro")
        else:
            if count == 0:
                self.view.error("El Contacto no exite")
            else:
                self.view.error("Problema al borrar el Contacto, Revisa")
        return