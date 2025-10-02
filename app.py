from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   

@app.route('/info')
def info():
    return {
        "materia": "Automatización de Infraestructura Digital",
        "profesor": "Froylan Alonso Perez", 
        "alumno": "Jocelyn Guadalupe Garcia Martinez",
        "carrera": "Ingeniería en Redes Inteligentes y Ciberseguridad"
    }

@app.route('/health')
def health_check():
    return {"status": "healthy", "message": "App funcionando correctamente"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)