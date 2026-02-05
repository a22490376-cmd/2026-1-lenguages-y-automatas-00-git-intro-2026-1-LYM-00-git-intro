# 📋 Ejercicios Progresivos: Guía de Referencia

Este documento lista los 4 ejercicios que practicarás a lo largo del curso.

---

## Ejercicio 1: Crear un Proyecto Local (Doc 04)

**Objetivo:** Familiarizarte con repositorios locales, commits y logs.

**Pasos:**
1. Crea una carpeta `Mi-Proyecto-1` en tu Desktop
2. Abre PowerShell y navega a la carpeta
3. Ejecuta `git init`
4. Crea un archivo `README.md` con:
   ```markdown
   # Mi Primer Proyecto Git
   Este es mi primer proyecto.
   ```
5. Ejecuta:
   ```bash
   git add README.md
   git commit -m "Crear proyecto inicial con README"
   ```
6. Crea un archivo `tareas.txt` con:
   ```
   - Tarea 1: Aprender Git
   - Tarea 2: Hacer proyecto
   ```
7. Ejecuta:
   ```bash
   git add tareas.txt
   git commit -m "Agregar lista de tareas"
   ```
8. Ejecuta `git log --oneline`
9. **Verificación:** Deberías ver 2 commits en el historial

---

## Ejercicio 2: Historial y Revertir (Doc 04)

**Objetivo:** Entender cómo Git rastrea cambios y puedes ver el historial.

**Pasos:**
1. Abre `tareas.txt` y agrega:
   ```
   - Tarea 3: Trabajar en equipo
   ```
2. Ejecuta:
   ```bash
   git add tareas.txt
   git commit -m "Agregar tarea de colaboración"
   ```
3. Ejecuta `git log --oneline`
4. **Verificación:** Deberías ver 3 commits

---

## Ejercicio 3: GitHub y Push (Doc 03/04)

**Objetivo:** Practicar conectar local a GitHub y subir código.

**Pasos:**
1. Crea un NUEVO repositorio en GitHub llamado "Mi-Proyecto-Practica"
2. En tu carpeta `Mi-Proyecto-1`, ejecuta:
   ```bash
   git remote add origin https://github.com/TuUsuario/Mi-Proyecto-Practica.git
   git branch -M main
   git push -u origin main
   ```
3. Ve a GitHub.com y abre tu repositorio
4. **Verificación:** Deberías ver:
   - Tu archivo `README.md`
   - Tu archivo `tareas.txt`
   - 3 commits en el historial

---

## Ejercicio 4: Simulación de Colaboración (Doc 05)

**Objetivo:** Practicar el flujo push/pull como si trabajaras en equipo.

**Pasos (Parte 1: Simular otro compañero):**
1. Ve a GitHub.com y abre tu repositorio
2. Abre `tareas.txt` y edítalo directamente en GitHub:
   - Haz clic en el icono de lápiz
   - Agrega una nueva línea: `- Tarea 4: Terminar proyecto`
   - Click en "Commit changes"
   - Escribe mensaje: "Agregar tarea 4 desde GitHub"

**Pasos (Parte 2: Simular recibir cambios):**
3. En PowerShell, en tu carpeta `Mi-Proyecto-1`:
   ```bash
   git pull origin main
   ```
4. Abre `tareas.txt` en tu editor
5. **Verificación:** Deberías ver la nueva línea "Tarea 4"

**Pasos (Parte 3: Hacer más cambios):**
6. Edita `tareas.txt` en tu computadora:
   - Agrega: `- Tarea 5: Celebrar éxito`
7. Ejecuta:
   ```bash
   git add tareas.txt
   git commit -m "Agregar tarea 5 desde mi computadora"
   git push
   ```
8. Ve a GitHub.com y actualiza la página
9. **Verificación:** Deberías ver la "Tarea 5" en GitHub

---

## Checkpoint: Ejercicios Completados

¿Completaste todos los ejercicios?

- [x] ✅ Ejercicio 1: Repositorio local con 2+ commits
- [x] ✅ Ejercicio 2: Historial con 3 commits
- [x] ✅ Ejercicio 3: GitHub tiene tus archivos
- [x] ✅ Ejercicio 4: Pull y push funcionan

Si completaste TODO → **Estás listo para el entregable final**
