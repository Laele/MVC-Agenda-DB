class View:
    """
    **************************
    * A view for a agenda DB *
    **************************
    """

    def start(self):
        print('=================================')
        print('= ¡Bienvenido a nuestra agenda! =')
        print('=================================')
    
    def end(self):
        print('===============')
        print('= ¡Nos vemos! =')
        print('===============')
    
    def main_menu(self):
        print("************************")
        print("* -- Menu Principal -- *")
        print("************************")
        print("1. Citas")
        print("2. Contactos")
        print("3. Salir")
    
    def option(self,last):
        print("Selecciona una opcion (1 - "+last+"'): ", end = "")
    
    def not_valid_option(self):
        print("¡Opcion no valida!\nIntenta de nuevo")
    
    def ask(self,output):
        print(output, end = "")
    
    def msg(self, output):
        print(output)
    
    def ok(self,id,op):
        print("+"*(len(str(id))+len(op)+24))
        print("+ ¡"+str(id)+" se "+op+" correctamente! +")
        print("+"*(len(str(id))+len(op)+24))
    
    def error(self,err):
        print(" ¡ERROR! ".center(len(err)+4, "-"))
        print("- "+err+" -")
        print("-"*(len(err)+4))

    """
    *******************
    * Views for citas *
    *******************
    """
    
    def citas_menu(self):
        print("***********************")
        print("* -- Submenu Citas -- *")
        print("***********************")
        print("1. Crear Cita")
        print("2. Mostrar Cita")
        print("3. Mostrar todas las Citas")
        print("4. Actualizar Cita")
        print("5. Borrar Cita")
        print("6. Mostrar Citas de Contacto")
        print("7. Regresar")
    
    def show_a_cita(self,record):
        print(f'{record[0]:<6}|{record[1]} |{record[2]:<35}|{record[3]:<20}|{record[4]:<35}')
        #print(f'{record[0]:<6}|{record[1]} |{record[2]:<35}|{record[3]:<20}|{record[4]+" "+record[5]+" "+record[6]:<35}')
        #print(record[1])
        #print(record)

    def show_cita_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(6)+"|"+"Fecha".ljust(20)+"|"+"Asunto".ljust(35)+"|"+"Ubicacion".ljust(20)+"|"+"Contacto".ljust(35))
        print("-"*120)
    
    def show_cita_midder(self):
        print("-"*120)
    
    def show_cita_footer(self):
        print("*"*120)
    
    """
    *******************
    * Views for contactos *
    *******************
    """
    def contactos_menu(self):
        print("***************************")
        print("* -- Submenu Contactos -- *")
        print("***************************")
        print("1. Crear Contacto")
        print("2. Mostrar Contacto")
        print("3. Mostrar todos los Contactos")
        print("4. Actualizar Contacto")
        print("5. Borrar Contacto")
        print("6. Regresar")
    
    def show_a_contacto(self, record):
        print("ID: ", record[0])
        print("Nombre: ",record[1])
        print("Apellido Paterno: ",record[2])
        print("Apellido Materno: ",record[3])
        print("Correo: ",record[4])
        print("Telefono: ",record[5])
    
    def show_contacto_header(self,header):
        print(header.center(48,"*"))
        print("-"*48)
    
    def show_contacto_midder(self):
        print("-"*48)
    
    def show_contacto_footer(self):
        print("*"*48)