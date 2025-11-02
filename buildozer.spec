[app]

# (str) Título de tu aplicación
title = Calculadora Kivy

# (str) Nombre del paquete (sin espacios ni acentos)
package.name = calculadora_kivy

# (str) Dominio del paquete (puedes inventarlo)
package.domain = org.ejemplo

# (str) Carpeta donde está el archivo main.py
source.dir = .

# (list) Archivos que se incluirán en el paquete
source.include_exts = py,png,jpg,kv,atlas

# (str) Versión de tu aplicación
version = 1.0

# (list) Librerías necesarias
requirements = python3,kivy

# (list) Orientación de la app (portrait = vertical)
orientation = portrait

# (bool) Pantalla completa o no (0 = no, 1 = sí)
fullscreen = 0

# (str) Formato del artefacto para el modo debug (APK)
android.debug_artifact = apk

# (list) Arquitecturas Android para compilar
android.archs = arm64-v8a, armeabi-v7a

# (bool) Permitir copia de seguridad (por defecto True)
android.allow_backup = True

