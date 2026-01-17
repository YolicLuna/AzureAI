# * Forma CORRECTA de instalar Azure CLI en Ubuntu 24.04 *

### *** 1.- Instalar dependencias: ***

sudo apt install ca-certificates curl apt-transport-https lsb-release gnupg


### *** 2.- Importar la clave de Microsoft: ***

sudo mkdir -p /etc/apt/keyrings
curl -sLS https://packages.microsoft.com/keys/microsoft.asc | \
  gpg --dearmor | sudo tee /etc/apt/keyrings/microsoft.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/microsoft.gpg


### *** 3.- Agregar el repositorio de Azure CLI: ***

AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] \
https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
sudo tee /etc/apt/sources.list.d/azure-cli.list


### *** 4.- Actualizar e instalar: ***

sudo apt update
sudo apt install azure-cli


### *** Verificar: ***

az version


### *** 5.- Inicia sesión con device code: ***

az login --use-device-code

### *** 5.2.- Abre el link manualmente: ***

- Copia el código
- Entra a: https://microsoft.com/devicelogin
- Inicia sesión con tu cuenta Microsoft
- Autoriza Azure CLI


### *** 6.- Verifica que ya estás autenticado: ***

az account show

### Debe devolver:

- id
- tenantId
- user.name
