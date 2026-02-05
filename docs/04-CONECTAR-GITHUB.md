# 3️⃣ Conectando Git a GitHub - Tu Primera Vez
> **Recuerda:** Al terminar este módulo, consulta y completa los ejercicios prácticos en [EJERCICIO.md](EJERCICIO.md) para reforzar lo aprendido.

⏱️ **Tiempo recomendado:** 10 minutos

**Objetivo:** Conectar tu Git local con tu repositorio en GitHub (el servidor).

**Prerequisito:** ✅ Debió haber completado los documentos 01 y 02 (Instalación + Conceptos)

---

## ¿Qué Haremos Hoy?

Hasta ahora:
- ✅ Instalaste Git en tu computadora
- ✅ Entiendes QUÉ es Git (repositorio, commit, rama)

**Hoy:**
- 🔗 Conectarás Git local con GitHub (el servidor)
- 📤 Aprenderás a subir tu código
- 📥 Aprenderás a descargar cambios

---

## 🎯 El Flujo de Conexión

```
Tu Computadora (Git local)
        ↕
    [INTERNET]
        ↕
GitHub.com (Git remoto)
```

**Conexión:**
- `git push` = Sube tus cambios a GitHub
- `git pull` = Descargas cambios de GitHub
- `git remote add` = Conecta tu local con GitHub

---

## Paso 1: Asumen que Tienes GitHub

Este curso asume que **ya tienes una cuenta en GitHub**. Si no:
1. Ve a https://github.com/signup
2. Crea tu cuenta (usa tu email)
3. Verifica tu email

Vuelve cuando tengas cuenta.

---

## Paso 2: Crear un Repositorio en GitHub

Vamos a crear un repositorio de prueba para practicar.

### 2.1 Abre GitHub.com

1. Inicia sesión en https://github.com
2. Haz clic en **"+"** (arriba a la derecha)
3. Selecciona **"New repository"**

### 2.2 Llena el Formulario

```
Repository name:  Mi-Primer-Repositorio
Description:      Prueba de Git y GitHub
Visibility:       Public (o Private si prefieres)
```

**Importante:** NO inicialices con README, .gitignore, o licencia. Déjalo vacío.

Haz clic en **"Create repository"**

---

## Paso 3: Conecta Tu Git Local

GitHub ahora te muestra 2 opciones:
- "...or push an existing repository from the command line"
- "...or create a new repository on the command line"

Copiarás los comandos de la PRIMERA opción.

### 3.1 Abre PowerShell/cmd

```bash
cd Desktop
mkdir mi-proyecto-git
cd mi-proyecto-git
```

### 3.2 Inicializa Git

```bash
git init
```

### 3.3 Crea un archivo README (opcional)

```bash
echo "# Mi Proyecto" > README.md
```

### 3.4 Haz tu primer commit

```bash
git add README.md
git commit -m "Commit inicial: crear proyecto"
```

### 3.5 Conecta con GitHub (LÍNEA CRÍTICA)

GitHub te mostró algo similar a:
```bash
git remote add origin https://github.com/TuUsuario/Mi-Primer-Repositorio.git
```

Copia y ejecuta EXACTAMENTE eso. Reemplaza `TuUsuario` con TU nombre de usuario.

**¿Qué significa?**
- `git remote add` = Conectar a un servidor remoto
- `origin` = El nombre del servidor (siempre "origin" por convención)
- `https://...` = La URL de tu repositorio en GitHub

### 3.6 Sube tu código

```bash
git branch -M main
git push -u origin main
```

**Primera ejecución:** Te pedirá autenticación. Usa tus credenciales de GitHub.

---

## ✅ ¿Funcionó?

Ve a GitHub.com y abre tu repositorio. Deberías ver:
- El archivo `README.md` en la página principal
- El commit que hiciste ("Commit inicial...")
- En "history" ves exactamente cuándo lo hiciste

Si ves eso: ✅ **¡Felicidades! Git y GitHub están conectados.**

---

## ¿Y si no Funcionó?

### Error: "Permission denied"

**Solución:**
- GitHub cambió la autenticación en 2021
- Necesitas un "Personal Access Token" en lugar de contraseña

1. Ve a: https://github.com/settings/tokens
2. Haz clic en "Generate new token"
3. Dale un nombre: "Mi Token"
4. Marca: `repo` (acceso completo)
5. Haz clic en "Generate"
6. **Copia el token** (no lo compartas)
7. Cuando PowerShell pida contraseña, pega el token

### Error: "fatal: could not read UserName"

**Solución:** No configuraste tu nombre en Git (te saltaste algun paso de [01-INSTALACION.md](01-INSTALACION.md)). Repasa esa lección. Luego intenta `git push` de nuevo.

### Error: "The remote repository is not empty"

**Solución:** GitHub no estaba vacío. **Borra el repo y crea uno nuevo.**

---

## 📚 Conceptos Nuevos

### `git remote`
Comando para manejar servidores remotos.

```bash
git remote add origin <URL>        # Conectar a un servidor
git remote -v                      # Ver los remotos conectados
git remote remove origin           # Desconectar
```

### `git branch -M main`
Cambia el nombre de la rama a `main` (estándar moderno).

### `git push -u origin main`
Sube tu rama `main` a GitHub.

---

## ✅ Checkpoints: Conectando a GitHub

### Checkpoint 1: Cuenta de GitHub Verificada ✅

- [x] Tengo una cuenta activa en GitHub
- [x] **Verificación:** Abre https://github.com y haz login
  - Deberías ver tu perfil con tu avatar
- [x] Si lograste iniciar sesión → ✅ Marca este checkpoint

### Checkpoint 2: Repositorio Creado en GitHub ✅

- [x] Creé un repositorio NUEVO en GitHub
- [x] **Verificación:** 
  - Ve a tu perfil (clic en tu avatar → "Your repositories")
  - Busca tu nuevo repositorio en la lista
  - Haz clic en él — debe estar vacío o con solo README.md
- [x] Si ves el repo → ✅ Marca este checkpoint

### Checkpoint 3: Git y GitHub Conectados ✅

- [x] En tu computadora, ejecuté `git remote add origin <URL>`
- [x] Ejecuté `git push -u origin main`
- [x] El push se completó sin errores
- [x] **Verificación Paso 1:**
  ```bash
  git remote -v
  ```
  Deberías ver:
  ```
  origin  https://github.com/TuUsuario/TuRepo.git (fetch)
  origin  https://github.com/TuUsuario/TuRepo.git (push)
  ```
- [x] **Verificación Paso 2:**
  - Ve a GitHub.com y abre tu repositorio
  - Deberías VER tu archivo README.md
  - En "history" o "commits" deberías ver tu commit
- [x] Si cumples AMBAS verificaciones → ✅ Marca este checkpoint

**¡Felicidades! Git local está conectado con GitHub. Ahora puedes colaborar.**

---

## 💾 Guarda tu Progreso

Ahora que completaste esta lección y marcaste todos los checkpoints, ejecuta estos comandos para guardar tu progreso en un commit y que el autograder te lo califique cuando hagas push.

```bash
git add docs/04-CONECTAR-GITHUB.md
git commit -m "Completo 04: Conectar Git a GitHub"
```

**Confirmación:** En tu terminal deberías ver:

```
[main xxxxxxx] Completo 04: Conectar Git a GitHub
 1 file changed, [X] insertions(+), [Y] deletions(-)
```

**Nota:** Este es el primer `git push` "real" de tu tarea/asignatura. Verifica que funciona.

---

## 🎯 Siguiente Paso

Ahora que tu local está conectado a GitHub, aprenderás a:
- Hacer commits locales
- Subirlos con `push`
- Descargar cambios con `pull`


---

**Siguiente paso:** Realiza los ejercicios correspondientes en [EJERCICIO.md](EJERCICIO.md) antes de continuar al siguiente módulo.

## 🔗 Navegación

← [Anterior: Por Qué Git Importa](./03-POR-QUE-GIT.md)

→ [Siguiente: Comandos Básicos](./05-COMANDOS-BASICOS-WINDOWS.md)
