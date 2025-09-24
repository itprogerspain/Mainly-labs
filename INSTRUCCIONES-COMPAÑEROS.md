# 📋 INSTRUCCIONES PARA COMPAÑEROS DE EQUIPO

## 🎯 Qué vas a encontrar
Juan ha dockerizado completamente la aplicación Django con autenticación LDAP. **Todo funciona automáticamente** sin instalaciones locales.

## 📥 Pasos para usar el sistema

### 1. Obtener el código
```bash
git clone <url-del-repositorio>
cd Mainly-labs
git checkout juanrra_implementacion_ldap
```

### 2. Configurar variables de entorno
```bash
# Crear archivo de configuración
cp .env.example .env
```
> **Nota**: Los valores por defecto funcionan perfectamente para desarrollo

### 3. Levantar el sistema completo
```bash
docker-compose up -d
```
> **⏱️ Primera vez**: Puede tardar 2-3 minutos descargando imágenes

### 4. Verificar que todo funciona
```bash
docker-compose ps
```
Deberías ver:
```
NOMBRE      ESTADO
web         Up
db          Up  
ldap        Up
phpldapadmin Up
```

### 5. Acceder a la aplicación
- **Aplicación**: http://localhost:8000
- **Usuario**: `admin` / **Contraseña**: `admin123`

## 🌟 ¿Qué tienes disponible?

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **App Django** | http://localhost:8000 | Aplicación principal |
| **phpLDAPAdmin** | http://localhost:8080 | Gestión visual del LDAP |

## 👥 Usuarios disponibles

| Usuario | Contraseña | Rol | Dashboard |
|---------|------------|-----|-----------|
| admin | admin123 | Administrador | Admin completo |
| testuser | testpass123 | Usuario normal | Dashboard usuario |

## 🔧 Comandos frecuentes

```bash
# Ver logs si algo falla
docker-compose logs web
docker-compose logs ldap

# Parar todo
docker-compose down

# Reiniciar solo un servicio
docker-compose restart web

# Ver estado en tiempo real
docker-compose logs -f web
```

## ⚠️ Posibles problemas y soluciones

### Puerto 8000 ocupado
```bash
# En docker-compose.yml cambiar:
ports:
  - "8001:8000"  # Cambiar 8000 por 8001
```

### LDAP no inicia
```bash
# Ver logs específicos
docker-compose logs ldap
# Reiniciar LDAP
docker-compose restart ldap
```

### Base de datos no conecta
```bash
# Reiniciar servicios en orden
docker-compose down
docker-compose up -d
```

## 📞 Contacto
Si algo no funciona, contacta a **Juan** - tiene toda la documentación técnica detallada.

---

**🎉 El sistema funciona completamente sin configuraciones adicionales!**  
*Solo necesitas Docker instalado en tu PC*