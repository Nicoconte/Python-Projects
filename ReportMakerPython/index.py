import time
from plyer import notification
from db_connector import *

class ReportMaker:
  def execute_query(self,d,conn):

    print("Inicio de la ejecucion ",d)
    while(True):
      if(d == "23:50"):
        conn = connector.get_connection()

        my_cursor = conn.cursor()
        my_cursor.execute("SELECT blogId,blogAuthor,blogTitle FROM bloginfo")

        myresult = my_cursor.fetchall()

        f = open("C:/Users/sunic/OneDrive/Documentos/reporte.csv","w")
        
        for i in myresult:
            text = " / ".join(i)
            f.write(text)
            f.write("\n")

        f.close()
        show_message()
        break
      else:
        print("Esperando a que se haga la hora")
        time.sleep(7)
      d = time.strftime("%H:%M")


#this show a message on desktop
def show_message():
  notification.notify(
      title='Hola usuario!',
      message='Su reporte fue generado!',
      timeout=5, 
  )



#Db objects
connector = db_connector()

#Date variable
date = time.strftime("%H:%M")

report = ReportMaker()

report.execute_query(date,connector)