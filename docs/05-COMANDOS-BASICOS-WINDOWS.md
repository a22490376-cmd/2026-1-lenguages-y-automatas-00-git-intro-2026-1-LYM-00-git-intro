# Git para Windows: Los Comandos Básicos 🪟

⏱️ **Tiempo recomendado:** 25 minutos

**Objetivo:** Aprender los 4 comandos esenciales que usarás todos los días.

Prerequisitos

✅ Debería estar instalado si completaste [01-INSTALACION.md](./01-INSTALACION.md)

Verifica que Git esté instalado abriendo **cmd.exe**, **PowerShell** o **Windows Terminal** y escribe:

```bash
git --version
```

Deberías ver algo como: `git version 2.40.0.windows.1`

Si no aparece nada, Git no está instalado correctamente. Regresa a la lección de instalación.

---

## 🎯 Los 4 Comandos Esenciales

Aquí están los ÚNICOS 4 comandos que necesitas aprender:

| Comando | ¿Qué hace? | Cuándo lo usas |
|---------|-----------|----------------|
| `git add` | Prepara archivos para guardar | Después de modificar archivos |
| `git commit` | Guarda los cambios con un mensaje | Cuando terminas una tarea |
| `git push` | Sube tus cambios al servidor | Para que tus compañeros vean tu trabajo |
| `git pull` | Descargas cambios de compañeros | Al iniciar o cuando compañeros subieron código |

---

## 📂 Configuración Inicial (hazlo UNA sola vez)

Antes de empezar, Git necesita saber quién eres:

### En Windows Terminal, PowerShell o cmd.exe:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@escuela.mx"
```

**Ejemplo:**
```bash
git config --global user.name "Paula Gómez"
git config --global user.email "paula.gomez@escuela.mx"
```

Esto dice: "Cuando Paula haga commits, están firmados por ella" 

✨ **Hazlo una sola vez y listo. Git nunca te lo volverá a pedir.**

---


## 🚀 Tu Primer Proyecto: Paso a Paso

Vamos a simular un proyecto real. Sigue estos pasos exactamente:

### Paso 1: Crea una carpeta para tu proyecto

En PowerShell o cmd.exe:

```bash
cd Desktop
mkdir MiProyectoGit
cd MiProyectoGit
```

**Explicación:**
- `cd Desktop` = ir a tu escritorio
- `mkdir MiProyectoGit` = crear una carpeta nueva
- `cd MiProyectoGit` = entrar en esa carpeta

### Paso 2: Inicializa el repositorio Git

```bash
git init
```

**¿Qué pasó?** Git creó una carpeta ".git" invisible que guarda todo el historial. No la toques nunca.

Verifica que funcionó:

```bash
dir
```

Deberías ver una carpeta oculta `.git` (si no la ves, activa "Ver archivos ocultos" en Windows)

### Paso 3: Crea tu primer archivo

Abre **Bloc de Notas** o tu editor favorito y crea un archivo llamado `main.py`:

```python
print("Hola, soy un programa")
```

Guárdalo en `C:\Users\TuUsuario\Desktop\MiProyectoGit\main.py`

### Paso 4: Dile a Git que observar el archivo

```bash
git add main.py
```

**¿Qué pasó?** Git ahora está "viendo" el archivo y preparándolo para guardar.

### Paso 5: Haz tu primer commit (guarda los cambios)

```bash
git commit -m "Crear archivo principal con hola mundo"
```

**Explicación:**
- `git commit` = "Voy a guardar cambios"
- `-m` = "Voy a escribir un mensaje"
- `"Crear archivo..."` = Tu mensaje describing qué hiciste

**Deberías ver algo como:**
```
[main (root-commit) a3f8c2h] Crear archivo principal con hola mundo
 1 file changed, 1 insertion(+)
 create mode 100644 main.py
```

✅ **¡Felicidades! Acabas de hacer tu primer commit!**

---

## 🔄 Flujo Normal: Cuando Trabajas

Ahora que tienes un proyecto, esto es lo que haces CADA VEZ que trabajas:

### 1️⃣ Modifica tus archivos

Abre `main.py` y cambia el código:

```python
print("Hola, soy un programa")
print("Estoy aprendiendo Git")
```

Guarda el archivo (Ctrl+S)

### 2️⃣ Ve qué archivos cambiaron

```bash
git status
```

**Deberías ver:**
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to stage changes)
        modified:   main.py
```

Esto significa: "Detecté que `main.py` cambió, pero no lo has guardado aún"

### 3️⃣ Prepara el archivo para guardar

```bash
git add main.py
```

O si cambiaste MUCHOS archivos:

```bash
git add .
```

(El `.` significa "añade TODO lo que cambió")

### 4️⃣ Guarda los cambios (commit)

```bash
git commit -m "Agregar segunda línea de print"
```

**Mensajes buenos vs malos:**

```bash
❌ git commit -m "cambios"
❌ git commit -m "asdjkl"
❌ git commit -m "x"

✅ git commit -m "Agregar segunda línea de print"
✅ git commit -m "Fix: enemigos no colisionaban"
```

El mensaje debe describir QUÉ HICISTE en presente.

---

## 👥 Trabajar en Equipo

Cuando trabajas con compañeros, necesitas 2 comandos adicionales:

### `git push` - Sube tus cambios

Después de hacer commits, subes tu trabajo para que otros lo vean:

```bash
git push
```

**¿Qué pasó?** Tus commits subieron a un servidor remoto (como GitHub, GitLab, etc.)

### `git pull` - Descargas cambios de otros

Antes de empezar a trabajar, descargas lo que tus compañeros subieron:

```bash
git pull
```

**¿Qué pasó?** Tu código local se actualiza con los cambios de tus compañeros

---

## 📊 Visualiza tu Historial

¿Quieres ver todos tus commits en una lista bonita?

```bash
git log --oneline
```

**Deberías ver algo como:**
```
a3f8c2h Agregar segunda línea de print
b9d1e5f Crear archivo principal con hola mundo
```

Cada línea es un commit. Los números son IDs únicos.

---

## ⚠️ Cosas Importantes para Windows

### 1. Rutas con Espacios

Si tu carpeta tiene espacios, Git puede confundirse. USE COMILLAS:

```bash
# ❌ Esto NO funciona si hay espacios
cd My Project

# ✅ Esto SÍ funciona
cd "My Project"
```

### 2. Mayúsculas

Windows NO es sensible a mayúsculas en nombres, pero Git SÍ. Cuidado:

```bash
❌ git add Main.py
✅ git add main.py
```

### 3. Codificación (Encoding)

A veces PowerShell usa UTF-16 por defecto. Si ves caracteres extraños:

```bash
# En PowerShell, ejecuta esto:
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```

### 4. Línea de Fin (Line Ending)

Windows usa `CR+LF` pero Linux/Mac usan `LF`. Git lo arregla automáticamente:

```bash
# En cmd.exe o PowerShell, ejecuta esto UNA sola vez:
git config --global core.autocrlf true
```

**No necesitas entender qué significa, solo hazlo una vez.**

---

## 🆘 Problemas Comunes y Soluciones

### Problema: "Git no reconoce el comando"

**Solución:** Git no está en el PATH. Reinstala Git y marca la opción:
- ✅ "Add Git to PATH"

Luego reinicia Windows Terminal/PowerShell.

---

### Problema: "Permission denied"

**Solución:** En PowerShell, ejecuta como administrador:
1. Abre PowerShell
2. Click derecho → "Ejecutar como administrador"
3. Intenta nuevamente

---

### Problema: "fatal: not a git repository"

**¿Qué pasó?** Intentaste un comando git en una carpeta que no tiene `.git`

**Solución:**
```bash
# Verifica que estés en la carpeta correcta
cd MiProyectoGit

# Y que tengas .git
dir
```

Si no ves `.git`, sigue el "Paso 2" de arriba:
```bash
git init
```

---

### Problema: "Changes not staged for commit"

**¿Qué pasó?** Modificaste un archivo pero olvidaste hacer `git add`

**Solución:**
```bash
git add .
git commit -m "Tu mensaje"
```

---

### Problema: FATAL - Escribí un mal mensaje en el commit

**Solución:** Para el último commit que hiciste:

```bash
git commit --amend -m "El mensaje CORRECTO"
```

**IMPORTANTE:** Solo hazlo si AÚN NO hiciste `git push`. Una vez subiste con `push`, no cambies los commits.

---

## 📋 Flujo Típico de un Día

Así es como usarás Git todos los días:

```bash
# MAÑANA - Al empezar a trabajar
git pull                          # Descargar cambios de compañeros

# Durante el día - Mientras trabajas
# [editas archivos en tu editor]
git status                        # Ver qué cambió
git add .                         # Preparar cambios
git commit -m "Descripción"       # Guardar cambios

# TARDE - Antes de irte
git push                          # Subir tus cambios
```

**Resumen:** PULL → TRABAJO → COMMIT → PUSH

---Checkpoint 10: Todo Dominado ✅

- [x] Entiendo qué es un commit
- [x] Puedo crear y ver un repositorio
- [x] Sé los 4 comandos esenciales
- [x] Puedo resolver problemas comunes
- [x] Completé el ejercicio práctico

---

## 

## 🎮 Ejercicio Práctico

Completa esto para practicar:

1. Crea una carpeta `Ejercicio1`
2. Haz `git init`
3. Crea un archivo `tareas.txt` con:
   ```
   - Tarea 1: Aprender Git
   - Tarea 2: Hacer proyecto
   ```
4. `git add tareas.txt`
5. `git commit -m "Crear lista de tareas"`
6. Modifica `tareas.txt` y añade:
   ```
   - Tarea 3: Colaborar con equipo
   ```
7. `git add tareas.txt`
8. `git commit -m "Agregar tarea de colaboración"`
9. Ejecuta `git log --oneline` y deberías ver 2 commits

Si ves 2 commits, ¡lo hiciste bien! ✅

---

## 📚 Referencia Rápida - Todos los Comandos en Una Página

```bash
# CONFIGURACIÓN (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@escuela.mx"

# CREAR REPOSITORIO
git init                          # Inicializar Git en una carpeta

# VER ESTADO
git status                        # Ver qué cambió
git log --oneline                # Ver historial de commits

# GUARDAR CAMBIOS
git add archivo.py                # Preparar UN archivo
git add .                         # Preparar TODOS los cambios
git commit -m "Mensaje"           # Guardar con mensaje

# TRABAJAR EN EQUIPO
git push                          # Subir mis cambios
git pull                          # Descargar cambios de otros

# EMERGENCIA
git commit --amend -m "nuevo"     # Cambiar último mensaje
```

---

## 🎯 Checkpoints de Aprendizaje

Completa los siguientes checkpoints antes de continuar:

### Checkpoint 1: Verificación Inicial ✅

- [x] Instalé Git correctamente (visto en documento 01)
- [x] Ejecuté `git --version` y funcionó
- [x] Configuré mi nombre y email con `git config`

### Checkpoint 2: Primer Repositorio ✅

- [x] Creé una carpeta llamada `MiProyectoGit`
- [x] Entré a esa carpeta con `cd MiProyectoGit`
- [x] Ejecuté `git init`
- [x] Verifiqué que existe la carpeta `.git`

### Checkpoint 3: Primer Commit Exitoso ✅

- [x] Creé un archivo `main.py` con contenido
- [x] Ejecuté `git add main.py`
- [x] Ejecuté `git commit -m "Crear archivo principal con hola mundo"`
- [x] Vi el mensaje de confirmación del commit

### Checkpoint 4: Commits Múltiples ✅

- [x] Ejecuté `git status` y entendí qué significa
- [x] Ejecuté `git add` en múltiples ocasiones
- [x] Hice al menos 2 commits con buenos mensajes
- [x] Ejecuté `git log --oneline` y vi mi historial

### Checkpoint 5: Conceptos de Equipo ✅

- [x] Entiendo qué es `git push`
- [x] Entiendo qué es `git pull`
- [x] Sé cuándo usar cada uno
- [x] Comprendo cómo Git sincroniza código entre personas

### Checkpoint 6: Windows-Específicas ✅

- [x] Entiendo cómo usar comillas en rutas con espacios
- [x] Sé que Windows es sensible a mayúsculas en Git
- [x] Configuré `core.autocrlf` si es necesario
- [x] Sé dónde buscar ayuda si algo falla

### Checkpoint 7: Problemas Comunes Resueltos ✅

- [x] Puedo resolver "git no reconoce el comando"
- [x] Sé qué hacer si tengo "Permission denied"
- [x] Entiendo "fatal: not a git repository"
- [x] Puedo arreglarlo si algo sale mal

### Checkpoint 8: Ejercicio Completado ✅

- [x] Completé el ejercicio práctico
- [x] Vi 2 commits en `git log --oneline`
- [x] Entiendo qué es un commit
- [x] Puedo crear y ver un repositorio

---

## 💾 Guarda tu Progreso en Git


Ahora que completaste esta lección y marcaste todos los checkpoints, ejecuta estos comandos para guardar tu progreso en un commit y que el autograder te lo califique cuando hagas push.

```bash
git add docs/05-COMANDOS-BASICOS-WINDOWS.md
git commit -m "Completo 05: Comandos Básicos de Git en Windows"
```

**Confirmación:** En tu terminal deberías ver:

```
[main xxxxxxx] Completo 05: Comandos Básicos de Git en Windows
 1 file changed, [X] insertions(+), [Y] deletions(-)
```

Una vez que veas el mensaje de confirmacion, no olvides ejecutar `git push` para que vayas viendo como el autograder va calificando tu progreso.



---

## 🔗 Navegación

**← Anterior:** [Por Qué Git Importa](./03-POR-QUE-GIT.md)

**→ Siguiente:** [Trabajo en Equipo y GitHub](./06-GITHUB-INTRO.md)
