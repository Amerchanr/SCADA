import subprocess

def run_script1():
    subprocess.Popen(['python', 'Interfaz.py'])

def run_script2():
    subprocess.Popen(['python', 'cliente3.py'])

if __name__ == '__main__':
    # Iniciar ambos scripts
    run_script1()
    run_script2()

    # Aquí puedes agregar cualquier otra lógica que necesites
    # Por ejemplo, esperar a que ambos scripts terminen (si es necesario)