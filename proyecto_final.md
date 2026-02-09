# Proyecto final de Modulo

### Nombre del Proyecto: API de Gestión de Finanzas Personales ("MyWallet")

**Objetivo:** Crear una API donde los usuarios puedan registrarse, iniciar sesión y gestionar sus ingresos y gastos personales. La clave es que **cada usuario solo puede ver y editar sus propios datos** (aislamiento de datos).

**Tiempo:** 7 dias (Jueves 5 de febrero)


### Requerimientos Técnicos (Stack)

- **Lenguaje:** Python
- **Framework:** Django & Django Rest Framework
- **Base de Datos:** PostgreSQL
- **Autenticación:** JWT (SimpleJWT)
- **Herramientas:** Insomnia para pruebas.

### Cronograma de Trabajo

### Configuración y Autenticación

- **Objetivo:** Tener el proyecto corriendo y usuarios registrándose.
- **Tareas:**
    1. Crear entorno virtual, instalar Django, DRF y SimpleJWT.
    2. Iniciar proyecto `mywallet` y app `finance`.
    3. Configurar base de datos y `settings.py` (apps instaladas, configuración JWT).
    4. Implementar **Registro de Usuarios** (Serializer y Vista pública).
    5. Configurar URLs para **Login** (Token Obtain) y Refresh.
    6. **Entregable:** Poder crear un usuario y obtener un Token en Postman.

### Modelado de Datos (Database)

- **Objetivo:** Definir la estructura de la información.
- **Tareas:**
    1. Crear modelo `Category` (Ej: Comida, Transporte, Salario).
        - Campos: `name`, `user` (ForeignKey - opcional, para categorías personalizadas).
    2. Crear modelo `Transaction` (La operación financiera).
        - Campos: `title`, `amount` (Decimal), `type` (Ingreso/Gasto), `date`, `category` (ForeignKey), `user` (ForeignKey - ¡Importante!).
    3. Hacer migraciones (`makemigrations`, `migrate`).
    4. Registrar modelos en el `admin.py` para verlos visualmente.

### Serializers y Vistas Básicas

- **Objetivo:** Traducir modelos a JSON y crear endpoints CRUD crudos.
- **Tareas:**
    1. Crear `CategorySerializer` y `TransactionSerializer`.
    2. Implementar `ModelViewSet` para Categorías y Transacciones.
    3. Configurar el `Router` en `urls.py`.
    4. **Prueba:** Verificar que puedes crear datos (aunque aún todos pueden ver los datos de todos).

### Lógica de Negocio y Protección (QuerySets)

- **Objetivo:** Que el usuario "Juan" solo vea los gastos de "Juan".
- **Tareas:**
    1. Añadir `permission_classes = [IsAuthenticated]` a los ViewSets.
    2. **Sobrescribir el método `get_queryset`** en los ViewSets
    3. **Sobrescribir el método `perform_create`**
      

### Filtros y Ordenamiento

- **Objetivo:** Hacer la API útil para consultas.
- **Tareas:**
    1. Permitir filtrar transacciones por tipo (sólo ingresos o sólo gastos).
        - *Tip:* Usar `django-filter` o sobrescribir `get_queryset` para leer parámetros de URL (ej: `?type=expense`).
    2. Permitir ordenar por fecha (las más recientes primero).

### Refinamiento y Dashboard (Opcional/Reto)

- **Objetivo:** Endpoints personalizados (no solo CRUD).
- **Reto:** Crear una vista personalizada (APIView) llamada `DashboardView`.
    - Debe devolver un JSON con el resumen:
    
    ```json
    {
        "total_income": 1500.00,
        "total_expense": 400.00,
        "balance": 1100.00
    }
    ```
    
    - *Pista:* Usarás `Transaction.objects.filter(...).aggregate(Sum('amount'))`.

### Pruebas Finales y Documentación

- **Objetivo:** Asegurar calidad.
- **Tareas:**
    1. Probar flujo completo en Postman:
        - Registro -> Login -> Crear Categoría -> Crear Gasto -> Intentar ver gasto sin token (Error) -> Ver Balance.
    2. Exportar la colección de Postman (para entregarla como documentación).
    3. Crear un archivo `README.md` explicando cómo instalar y correr el proyecto.

### Estructura de Datos Sugerida (Models.py)

Para ayudarte a empezar, aquí tienes una guía de los modelos clave:

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Opcional: Si quieres categorías globales, deja user como null
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('INCOME', 'Ingreso'),
        ('EXPENSE', 'Gasto'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (${self.amount})"
```

### Endpoints Finales Esperados

Al terminar, tu API debería tener estas rutas funcionando:

1. `POST /api/register/` (Crear usuario)
2. `POST /api/token/` (Login - Obtener JWT)
3. `POST /api/token/refresh/` (Refrescar JWT)
4. `GET /api/categories/` (Listar categorías)
5. `POST /api/categories/` (Crear categoría)
6. `GET /api/transactions/` (Ver mis movimientos - Protegido)
7. `POST /api/transactions/` (Registrar movimiento - Protegido)
8. `DELETE /api/transactions/{id}/` (Borrar movimiento - Protegido)
9. *(Extra)* `GET /api/dashboard/` (Ver balance total)