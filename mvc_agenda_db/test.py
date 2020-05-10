#from model.model import Model

#m = Model()

#m.create_contacto("1","Luis","Soriano","Crespo","luis.sorianocrespo@outlook.com","4641145785")
#m.create_contacto("2","Alan","Alvarez","Sanchez","alan.alvsa@outlook.com","4641135864")

#data = m.read_all_contactos()
#print(data)

#m.update_contacto('2','chester','','','','4649999999')

#data = m.read_all_contactos()
#print(data)

#data = m.read_a_contacto("1")
#print(data)
#m.delete_contacto("1")

#data = m.read_all_contactos()
#print(data)

#m.create_cita("2020-06-01 12:00:00","Regreso a Clases","DICIS","2")
#data = m.read_a_cita("1")
#print(data)
################################
from controller.controller import Controller

c = Controller()
c.start()

#m.close_db()