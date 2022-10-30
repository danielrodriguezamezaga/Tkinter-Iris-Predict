
# Exercise FastApi of: Daniel Rodríguez Amézaga
import tkinter as tk
import pickle

ventana = tk.Tk()

# Importo el modelo ya entrenado desde jupyter NoteBook
model = pickle.load(open('savemodel.sav', 'rb'))

# Creo la funcion Predict y muestro los valores insertados y seguidamente la predicción.
def predict():
    print("sepal_length: ", sepal_length.get(), 
          "- sepal_width:", sepal_width.get(),
          "- petal_length:", petal_length.get(),
          "- petal_width:", petal_width.get())
    result = model.predict([[sepal_length.get(), sepal_width.get(), 
                             petal_length.get(), petal_width.get()]])[0]
    print(result)
    
    sepal_length.delete(0, tk.END)
    sepal_width.delete(0, tk.END)
    petal_length.delete(0, tk.END)
    petal_width.delete(0, tk.END)

ventana.title("ubicacioón en la pantalla")
ventana.geometry("350x350")

ventana.resizable(0,0)

tk.Label(ventana, text="Ingrese los datos:").grid(row=1, column=0)
tk.Label(ventana, text=" Sepal Length ").grid(row=2, column=0)
tk.Label(ventana, text=" Sepal width").grid(row=3, column=0)
tk.Label(ventana, text=" Petal Length").grid(row=4, column=0)
tk.Label(ventana, text=" Petal width").grid(row=5, column=0)

sepal_length = tk.Entry(ventana)
sepal_length.insert(0, "")
sepal_length.grid(row=2, column=1)

sepal_width = tk.Entry(ventana)
sepal_width.insert(0, "")
sepal_width.grid(row=3, column=1)

petal_length = tk.Entry(ventana)
petal_length.insert(0, "")
petal_length.grid(row=4, column=1)

petal_width = tk.Entry(ventana)
petal_width.insert(0, "")
petal_width.grid(row=5, column=1)

tk.Button(ventana, text="Predict",
          fg="white", bg="blue", command=predict).grid(row=6, column=0)

tk.mainloop()