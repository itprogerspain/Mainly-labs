# Configuración LDAP con Docker - Guía para el Equipo

## Resumen
Este documento explica cómo configurar y usar el sistema LDAP usando Docker Compose para que todo el equipo pueda trabajar con la implementación LDAP sin necesidad de instalar servicios localmente.

## Configuración Rápida

### 1. Clonar el repositorio y preparar el entorno
```bash
git clone https://github.com/itprogerspain/Mainly-labs.git
cd Mainly-labs
git checkout juanrra_implementacion_ldap
```

### 2. Crear archivo .env
```bash
cp .env.example .env
```

### 3. Levantar todos los servicios
```bash
docker-compose up -d
```

Esto levantará:
- **PostgreSQL** (base de datos): puerto 5432
- **Django App**: puerto 8000
- **LDAP Server**: puerto 389
- **LDAP Admin Interface**: puerto 8080

### 4. Configurar LDAP inicial (solo la primera vez)
```bash
# Esperar que LDAP esté listo
sleep 10

# Cargar grupos iniciales
docker-compose exec ldap ldapadd -x -D "cn=admin,dc=example,dc=com" -w admin_password -f /container/service/slapd/assets/config/bootstrap/ldif/custom/ldap_groups.ldif
```

### 5. Acceder a las interfaces
- **Django App**: http://localhost:8000
- **LDAP Admin**: http://localhost:8080
  - Server: ldap
  - Username: cn=admin,dc=example,dc=com
  - Password: admin_password

## Servicios Disponibles

### Django Application (puerto 8000)
- Login: http://localhost:8000/accounts/login/
- Admin LDAP: http://localhost:8000/admin/ldap/
- Dashboard: http://localhost:8000/dashboard/

### LDAP Server (puerto 389)
- **Host**: ldap://localhost:389
- **Admin DN**: cn=admin,dc=example,dc=com
- **Password**: admin_password
- **Base DN**: dc=example,dc=com

### PhpLDAPAdmin (puerto 8080)
Interface web para gestionar LDAP directamente:
- **URL**: http://localhost:8080
- **Server**: ldap
- **Login DN**: cn=admin,dc=example,dc=com
- **Password**: admin_password

## Comandos Útiles

### Verificar servicios
```bash
docker-compose ps
```

### Ver logs
```bash
# Todos los servicios
docker-compose logs

# Solo LDAP
docker-compose logs ldap

# Solo Django
docker-compose logs web
```

### Restart servicios
```bash
docker-compose restart
```

### Parar servicios
```bash
docker-compose down
```

### Limpiar completamente (elimina datos)
```bash
docker-compose down -v
```

## Crear Usuarios LDAP

### Desde Django Admin
1. Ir a http://localhost:8000/admin/ldap/
2. Hacer clic en "Crear Usuario LDAP"
3. Llenar formulario y guardar

### Desde línea de comandos
```bash
# Crear usuario manualmente
docker-compose exec ldap ldapadd -x -D "cn=admin,dc=example,dc=com" -w admin_password << EOF
dn: uid=testuser,ou=users,dc=example,dc=com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
uid: testuser
sn: User
givenName: Test
cn: Test User
displayName: Test User
uidNumber: 1001
gidNumber: 1001
userPassword: {SSHA}password_hash_here
loginShell: /bin/bash
homeDirectory: /home/testuser
mail: testuser@example.com
EOF
```

## Troubleshooting

### LDAP no se conecta
```bash
# Verificar que LDAP está corriendo
docker-compose ps ldap

# Verificar logs de LDAP
docker-compose logs ldap

# Reiniciar LDAP
docker-compose restart ldap
```

### Base de datos no conecta
```bash
# Verificar PostgreSQL
docker-compose ps db

# Verificar conexión desde Django
docker-compose exec web python manage.py dbshell
```

### Reset completo
```bash
# Parar todo
docker-compose down -v

# Eliminar imágenes si es necesario
docker-compose down -v --rmi all

# Volver a levantar
docker-compose up -d
```

## Estructura de Datos LDAP

### Base DN
- **dc=example,dc=com**

### Organizational Units
- **ou=users,dc=example,dc=com** - Usuarios
- **ou=groups,dc=example,dc=com** - Grupos

### Grupos Predefinidos
- **cn=active,ou=groups,dc=example,dc=com** - Usuarios activos
- **cn=staff,ou=groups,dc=example,dc=com** - Staff de Django
- **cn=superuser,ou=groups,dc=example,dc=com** - Superusuarios

## Variables de Entorno Importantes

En tu archivo `.env`:

```bash
# Database (usa 'db' como host en Docker)
DB_HOST=db

# LDAP (usa 'ldap' como host en Docker)
AUTH_LDAP_SERVER_URI=ldap://ldap:389
AUTH_LDAP_BIND_DN=cn=admin,dc=example,dc=com
AUTH_LDAP_BIND_PASSWORD=admin_password
```

## Notas Importantes

1. **Datos Persistentes**: Los datos de LDAP y PostgreSQL se guardan en volúmenes Docker
2. **Networking**: Los servicios se comunican usando nombres de servicio (ldap, db, web)
3. **Puertos**: Solo exponemos los puertos necesarios al host
4. **Seguridad**: En producción, cambiar todas las contraseñas por defecto

## Soporte

Si tienes problemas:
1. Verificar que Docker y Docker Compose están instalados
2. Revisar logs con `docker-compose logs`
3. Contactar a Juan (aljuanrra914@gmail.com) para dudas específicas de LDAP