# 1️⃣ Instalación de Git en Windows

⏱️ **Tiempo recomendado:** 10 minutos

**Objetivo:** Que Git esté listo en tu computadora con las claves SSH configuradas.


## Instalando Winget

Necesitarás instalar Git. La manera más sencilla de instalar Git en tu máquina Windows es usando **Winget** (el gestor de paquetes de Microsoft).

Abre una ventana de PowerShell o Windows Terminal y escribe el comando:

```powershell
winget
```

Si ves un mensaje como este:

> `winget : El término 'winget' no se reconoce como nombre de un cmdlet`

Significa que Winget no está instalado. Sigue la guía de instalación oficial desde Microsoft:  
https://learn.microsoft.com/es-es/windows/package-manager/winget/

Si Winget **sí funciona**, verás la ayuda y podrás continuar.


## Instalación de Git

Una vez que tienes Winget instalado, instala Git con este comando simple:

```powershell
winget install -e --id Git.Git
```

Espera a que la instalación termine. Esto puede tomar 1-2 minutos.

Para verificar que funcionó, abre una nueva terminal y ejecuta:

```powershell
git --version
```

Deberías ver algo como: `git version 2.40.0.windows.1`


## Configuración de Nombre y Correo

Una vez instalado, Git necesita saber quién eres. Configúralo con tus datos:

```powershell
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu.email@example.com"
```

**Ejemplo:**
```powershell
git config --global user.name "Paula Gómez"
git config --global user.email "paula.gomez@escuela.mx"
```

⚠️ **Importante:** Usa el email que registraste en GitHub. Esto asegura que tus commits se asocien correctamente a tu cuenta.


## Configuración de SSH (La Parte Importante)

La forma más segura de conectar con GitHub es usando **SSH** - un protocolo que usa pares de llaves (publica/privada) para autenticación.

### Paso 1: Generar la llave SSH

Ejecuta este comando en PowerShell:

```powershell
ssh-keygen -t ed25519 -C "tu.email@example.com"
```

Reemplaza el email con el tuyo (el mismo que usaste en el paso anterior).

Cuando se te pregunte, **solo presiona Enter** para todas las preguntas:

Se verá así:

```PowerShell
PS C:\> ssh-keygen -t ed25519 -C "paula.gomez@escuela.mx"
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\paula\.ssh\id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\paula\.ssh\id_ed25519
Your public key has been saved in C:\Users\paula\.ssh\id_ed25519.pub
```

### Paso 2: Ver tu llave pública

Desplega tu llave pública con:

```powershell
notepad $env:USERPROFILE\.ssh\id_ed25519.pub
```

Se abrirá un Notepad con tu llave. **Cópiala todo** (Ctrl+A, Ctrl+C).

### Paso 3: Añadir la llave a GitHub

1. Ve a https://github.com/settings/keys
2. Haz clic en **"New SSH Key"**
3. En **Title**, escribe algo descriptivo: "Mi Laptop Windows"
4. En **Key**, pega tu llave pública (la que copiaste)
5. Haz clic en **"Add SSH Key"**

### Paso 4: Probar la conexión SSH

Ahora verifica que todo funciona:

```powershell
ssh -T git@github.com
```

Si todo está bien, verás:

```
Hi TuUsuario! You've successfully authenticated, but GitHub does not provide shell access.
```

Si ves esto, ¡felicidades! SSH está configurado.


## ✅ Checkpoints: Verificación de Pasos

Completa cada checkpoint y verifica que funcionó:

### Checkpoint 1: Winget Instalado ✅

```powershell
winget
```

- [x] El comando winget esta instalado y lo puedo ejecutar desde la linea de comandos


### Checkpoint 2: Git Instalado ✅

Ejecuta el comando en la consola para verificar que git esta instalado. Marca la casilla si se imprime la version de git en al consola.

```powershell
git --version
```

- [x] Git esta instalado y puedo ejecutarlo y veo la version en la consola.

### Checkpoint 3: Identidad Configurada ✅

Revisa que tu identidad de git esta configurada. Ejecuta el siguiente comando:

```powershell
git config --global --list
```

Deberias ver algo similar a lo siguiente, pero con tu información.

```
user.name=Mi Nombre Completo
user.email=mi.email@escuela.mx
```

- [x] Ya configuré mi nombre y correo en git y lo puedo ver en la consola.


### Checkpoint 4: SSH Generado ✅

Verifica que ya generaste tu llave SSH. **Este paso es importantísimo**.

```powershell
dir $env:USERPROFILE\.ssh\
```

Deberías ver estos dos archivos en el listado de directorio

```
id_ed25519
id_ed25519.pub
```

- [x] Generé mi par de llaves SSH y las puedo ver listadas en el directorio `$env:USERPROFILE\.ssh\`


### Checkpoint 5: SSH Conectado a GitHub ✅

Vuelve a ejecutar este comando:

```powershell
ssh -T git@github.com
```

Deberías de poder ver de nuevo este mensaje:

```
Hi TuUsuario! You've successfully authenticated, but GitHub does not provide shell access.
```

- [x] Activa esta casilla si viste el mensaje de confirmación de que tu conexión a GitHub se puede completar.


## 💾 Guarda tu Progreso en Git

Ahora que completaste esta lección y marcaste todos los checkpoints, ejecuta estos comandos para guardar tu progreso en un commit y que el autograder te lo califique cuando hagas push.

```bash
git add docs/01-INSTALACION.md
git commit -m "Completo 01: Instalación de Git con SSH"
```

**Confirmación:** En tu terminal deberías ver:

```
[main xxxxxxx] Completo 01: Instalación de Git con SSH
 1 file changed, [X] insertions(+), [Y] deletions(-)
```

## 🎯 Resumen de qué aprendiste

✅ Instalaste Git con Winget  
✅ Configuraste tu identidad en Git  
✅ Generaste un par de llaves SSH  
✅ Conectaste Git con GitHub  

**¡Felicidades!** Tu computadora ahora está lista para usar Git. Pasemos a entender QUÉ ES Git y POR QUÉ lo necesitas.


## 🔗 Navegación

← [Inicio](../README.md) | [¿Qué es Git?](./02-QUE-ES-GIT.md) →
