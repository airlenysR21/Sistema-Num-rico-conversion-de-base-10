import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox



########################################################################

class VentanaBinario(tk.Toplevel):
   
    #----------------------------------------------------------------------
    def __init__(self, Ventbianrio):
        self.Ventbinario = Ventbianrio
        tk.Toplevel.__init__(self)
        self.title("Sistema Binario")
        self.geometry("500x600")
        self.config(bg="#DFEFF0")
        self.decimal=tk.StringVar()
        self.NumConv=tk.StringVar()
        

        #Titulos
        Titulo=tk.Label (self, text="Sistema Numérico", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",35 ))
        Titulo.place(x=20, y=40)

        Titulo2=tk.Label (self, text="conversión de base 10 a", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",25 ))
        Titulo2.place(x=50, y=90)

        Subtitulo=tk.Label (self, text="binario", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",25))
        Subtitulo.place(x=180, y=135)

        #Entrada
        info=tk.Label (self, text="Ingresa el número decimal", fg="#20664A", bg="#DEF0FC") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=110, y=230)
 
        self.EntradaDec=Entry(self, textvariable= self.decimal)
        self.EntradaDec.place(x=170, y=280)


        #Botón
        Convertir=tk.Button(self, text="Convertir", width=15 , command=self.decimal_a_binario)
        Convertir.place(x=170, y=320)

        regresar=tk.Button(self, text="Regresar", width=15,  command=self.onClose)
        regresar.place(x=320, y=550)

        Otro=tk.Button(self, text="Resetear", width=15 , command=self.reset)
        Otro.place(x=70, y=550)

        #Salida
        Salidainfo=tk.Label (self, text="El numero convertido en binario es:", fg="#20664A", bg="#DEF0FC") 
        Salidainfo.config(font=("Segoe UI Black",15))
        Salidainfo.place(x=80, y=390)
    
        self.Pantalla = tk.Label(self, foreground="white", background="black", width=30, height=2, textvariable= self.NumConv) 
        self.Pantalla.place(x=125, y=440)
        
    #----------------------------------------------------------------------
    def decimal_a_binario(self):
        try:
            decBinario = int(self.decimal.get())
            binario = ""

            if decBinario < 0:
                MessageBox.showerror("Error", "El numero debe ser entero positivo ")

            elif decBinario > 4096:
                MessageBox.showerror("Error", "El numero sobrepasa la cantidad que puede representar el sistema")
            
            else:
                while decBinario > 0:
                    residuo = decBinario % 2
                    binario = str(residuo) + binario
                    decBinario = int(decBinario/ 2)
                return self.NumConv.set(binario)
    
        except ValueError:
                MessageBox.showerror("Error", "Debe ingresar un numero entero")

    #----------------------------------------------------------------------
    def onClose(self):
        self.destroy()
        self.Ventbinario.show()

    def reset(self):
        self.EntradaDec.delete(0, "end")
        self.NumConv.set(0)
       

########################################################################

class VentanaOctal(tk.Toplevel):
   
    #----------------------------------------------------------------------
    def __init__(self, Ventoctal):
        self.Ventoctal = Ventoctal
        tk.Toplevel.__init__(self)
        self.title("Sistema Binario")
        self.geometry("500x600")
        self.config(bg="#DFEFF0")
        self.decimal=tk.StringVar()
        self.NumConv=tk.StringVar()

        regresar=tk.Button(self, text="Regresar", width=15,  command=self.onClose)
        regresar.place(x=320, y=550)

        #Titulos
        Titulo=tk.Label (self, text="Sistema Numérico", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",35 ))
        Titulo.place(x=20, y=40)

        Titulo2=tk.Label (self, text="conversión de base 10 a", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",25 ))
        Titulo2.place(x=50, y=90)

        Subtitulo=tk.Label (self, text="octal", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",25))
        Subtitulo.place(x=180, y=135)

        #Entrada
        info=tk.Label (self, text="Ingresa el número decimal", fg="#20664A", bg="#DEF0FC") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=110, y=230)

        self.EntradaOct=Entry(self, textvariable= self.decimal)
        self.EntradaOct.place(x=170, y=280)

        #Botón
        Convertir=tk.Button(self, text="Convertir", width=15 , command=self.decimal_a_octal)
        Convertir.place(x=170, y=320)

        regresar=tk.Button(self, text="Regresar", width=15,  command=self.onClose)
        regresar.place(x=320, y=550)

        Otro=tk.Button(self, text="Resetear", width=15 , command=self.reset)
        Otro.place(x=70, y=550)


        #Salida
        Salidainfo=tk.Label (self, text="El numero convertido en octal es:", fg="#20664A", bg="#DEF0FC") 
        Salidainfo.config(font=("Segoe UI Black",15))
        Salidainfo.place(x=80, y=390)

        Pantalla = tk.Label(self, foreground="white", background="black", width=30, height=2, textvariable= self.NumConv)  
        Pantalla.place(x=125, y=440)

    #----------------------------------------------------------------------
    def decimal_a_octal(self):
        try:
            decOctal = int(self.decimal.get())
            octal = ""

            if decOctal < 0:
                MessageBox.showerror("Error", "El numero debe ser entero positivo ")

            elif decOctal > 4096:
                MessageBox.showerror("Error", "El numero sobrepasa la cantidad que puede representar el sistema")
            
            else:
        
                while decOctal > 0:
                    residuo = decOctal % 8
                    octal = str(residuo) + octal
                    decOctal = int(decOctal / 8)
                return self.NumConv.set(octal)
                
        except ValueError:
                MessageBox.showerror("Error", "Debe ingresar un numero entero")

    #----------------------------------------------------------------------
    def onClose(self):
        self.destroy()
        self.Ventoctal.show()

    #----------------------------------------------------------------------
    def reset(self):
       self.EntradaOct.delete(0, "end")
       self.NumConv.set(0)

########################################################################

class VentanaHexadecimal(tk.Toplevel):
   
    #----------------------------------------------------------------------
    def __init__(self, Venthexadecimal):
        self.Venthexadecimal = Venthexadecimal
        tk.Toplevel.__init__(self)
        self.title("Sistema Binario")
        self.geometry("500x600")
        self.config(bg="#DFEFF0")
        self.decimal=tk.StringVar()
        self.NumConv=tk.StringVar()

        #Titulos
        Titulo=tk.Label (self, text="Sistema Numérico", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",35 ))
        Titulo.place(x=20, y=40)

        Titulo2=tk.Label (self, text="conversión de base 10 a", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",25 ))
        Titulo2.place(x=50, y=90)

        Subtitulo=tk.Label (self, text="hexadecimal", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",25))
        Subtitulo.place(x=180, y=135)

        #Entrada
        info=tk.Label (self, text="Ingresa el número decimal", fg="#20664A", bg="#DEF0FC") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=110, y=230)

        self.EntradaHex=Entry(self, textvariable= self.decimal)
        self.EntradaHex.place(x=170, y=280)

        #Botón
        Convertir=tk.Button(self, text="Convertir", width=15 , command=self.decimal_a_hexadecimal)
        Convertir.place(x=170, y=320)

        regresar=tk.Button(self, text="Regresar", width=15,  command=self.onClose)
        regresar.place(x=320, y=550)
        
        Otro=tk.Button(self, text="Resetear", width=15 , command=self.reset)
        Otro.place(x=70, y=550)


        #Salida
        Salidainfo=tk.Label (self, text="El numero convertido en hexadecimal es:", fg="#20664A", bg="#DEF0FC") 
        Salidainfo.config(font=("Segoe UI Black",15))
        Salidainfo.place(x=40, y=390)

        Pantalla = tk.Label(self, foreground="white", background="black", width=30, height=2, textvariable=  self.NumConv)  
        Pantalla.place(x=125, y=440)

 #----------------------------------------------------------------------
    def obCaracter(valor):
        valor = str(valor)
        equiv = { "10": "A", "11": "B", "12": "C","13": "D", "14": "E","15": "F"}
        if valor in equiv:
            return equiv[valor]
        else:
            return valor

    #----------------------------------------------------------------------
    def decimal_a_hexadecimal(self):
        try:
            dechexadecimal= int(self.decimal.get())
            hexadecimal = ""

            if dechexadecimal < 0:
                MessageBox.showerror("Error", "El numero debe ser entero positivo ")

            elif dechexadecimal > 4096:
                MessageBox.showerror("Error", "El numero sobrepasa la cantidad que puede representar el sistema")
            
            else:
                while dechexadecimal > 0:
                    residuo = dechexadecimal % 16
                    Caracter = VentanaHexadecimal.obCaracter(residuo)
                    hexadecimal = Caracter + hexadecimal
                    dechexadecimal = int(dechexadecimal / 16)
                return self.NumConv.set(hexadecimal)

        except ValueError:
            MessageBox.showerror("Error", "Debe ingresar un numero entero")


    #----------------------------------------------------------------------
    def onClose(self):
        self.destroy()
        self.Venthexadecimal.show()

    def reset(self):
        self.EntradaHex.delete(0, "end")
        self.NumConv.set(0)

########################################################################
class principal(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, Ventana):
        """Constructor"""
        self.vent = Ventana
        self.vent.title("Sistema Binario")
        self.vent.config(bg="#DFEFF0")

        Titulo=Label (self.vent, text="Sistema Numérico", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",35 ))
        Titulo.place(x=20, y=50)

        Titulo2=tk.Label (self.vent, text="conversión de base 10 a", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",25 ))
        Titulo2.place(x=50, y=100)

        Subtitulo=tk.Label (self.vent, text="binario, octal y hexadecimal", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",18))
        Subtitulo.place(x=75, y=145)

        ##Info
        Info=tk.Label (self.vent, text="Selecciona en que base que deseas convertir el decimal", fg="#002060", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",13))
        Info.place(x=15, y=230)

        Info=tk.Label (self.vent, text="Creadores", fg="#7D9C9F", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",10))
        Info.place(x=200, y=525)

        Info=tk.Label (self.vent, text="Airlenys Recuero , Gabriela Vásquez", fg="#7D9C9F", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",10))
        Info.place(x=120, y=550)
        
        ##Botones
        Binario=tk.Button(self.vent, text="Binario", width=15, command=self.openBinario)
        Binario.place(x=180, y=300)
        
        Octal=tk.Button(self.vent, text="Octal", width=15, command=self.openOctal)
        Octal.place(x=180, y=370)

        Hexadecimal=tk.Button(self.vent, text="Hexadecimal", width=15, command=self.openHexadecimal)
        Hexadecimal.place(x=180, y=440)

        Cerrar=tk.Button(self.vent, text="Cerrar", width=10, command=self.cerrar)
        Cerrar.place(x=380, y=550)
    #----------------------------------------------------------------------

    def cerrar(self):
        self.vent.destroy()

    def openBinario(self):
        self.vent.withdraw()
        VentanaBinario(self)

    def openOctal(self):
        self.vent.withdraw()
        VentanaOctal(self)

    def openHexadecimal(self):  
        self.vent.withdraw()
        VentanaHexadecimal(self)
      
    #----------------------------------------------------------------------
    def show(self):
        self.vent.update()
        self.vent.deiconify()
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    Ventana = tk.Tk()
    Ventana.geometry("500x600")
    app = principal(Ventana)
    Ventana.mainloop()