<div align="center">

# ETL_Ecommnerce_ProyectoFinal 
### Arquitectura Medallion en Azure Databricks

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

*Pipeline automatizado de datos para análisis de ventas de un Ecommerce con arquitectura de tres capas y despliegue continuo*

</div>

---

## 🎯 Descripción

Pipeline ETL_Ecommnerce_ProyectoFinal toma los datos crudos de un ecommerce en formato csv (fuente kaggle) y genera indicadores de ventas por distintas categorias, implementando la **Arquitectura Medallion** (Bronze-Silver-Golden) en Azure Databricks con **CI/CD completo** y **Delta Lake** para garantizar consistencia ACID.

### ✨ Características Principales

- 🔄 **ETL Automatizado** - Pipeline completo con despliegue automático via GitHub Actions
- 🏗️ **Arquitectura Medallion** - Separación clara de capas Bronze → Silver → Golden
- 🚀 **CI/CD Integrado** - Deploy automático en cada push a master
- 📈 **Databricks Dashboards** - Visualización

---

## 🏛️ Arquitectura

### Flujo de Datos

```
📄 CSV (Raw Data)
    ↓
🥉 Bronze Layer (Ingesta sin transformación)
    ↓
🥈 Silver Layer (Limpieza + Tabla Matriz de Ventas)
    ↓
🥇 Golden Layer (Agregaciones de Negocio)
    ↓
📊 Databricks Dashboards (Visualización)
```

![Texto descriptivo](Arquitectura.png)


### 📦 Capas del Pipeline

<table>
<tr>
<td width="33%" valign="top">

#### 🥉 Bronze Layer
**Propósito**: Zona de aterrizaje

**Tablas**: 
- `customer_detail` 
- `ecommerce_sales` 
- `product_detail`

**Características**:
- ✅ Datos tal como vienen de origen
- ✅ Timestamp de ingesta
- ✅ Sin validaciones

</td>
<td width="33%" valign="top">

#### 🥈 Silver Layer
**Propósito**: Modelo dimensional

**Tablas**:
- `ecommerce_sales` 

**Características**:
- ✅ Generacion de Tabla consolidada de ventas
- ✅ Datos normalizados
- ✅ Validaciones completas

</td>
<td width="33%" valign="top">

#### 🥇 Golden Layer
**Propósito**: Analytics-ready

**Tablas**:
- ingresos_por_categoria    : Monto total en ventas agrupado por categoría
- ingresos_por_estado       : Monto total en ventas agrupado por locación(Estado)
- ingresos_por_genero       : Monto total en ventas agrupado genero (Hombre - Mujer)
- ingresos_por_suscripcion  : Monto total en ventas agrupado suscripcion (Si - No)
**Características**:
- ✅ Pre-agregados
- ✅ Optimizado para BI
- ✅ Performance máximo

</td>
</tr>
</table>

---

## 📁 Estructura del Proyecto

```
etl-apple/
│
├── 📂 .github/
│   └── 📂 workflows/
│       └── 📄 deploy-notebook.yml    # Pipeline CI/CD deploy workspace databricks
├── 📂 certificacione/
    └── 📄 Certificacion Databriks Fundamentals.pdf        # Certificado de Databriks Fundamentals
    └── 📄 Certificacion Generative AI Fundamentals.pdf    # Certificado de Databriks Generative AI Fundamentals
    └── 📄 Links_Certificaciones                           # Links de Certificaciones Realizadas en DataBriks 
├── 📂 dataset/
    └── 📄 customer_details.csv
    └── 📄 EcommereceSales2024.csv
    └── 📄 product_details.csv       
├── 📂 evidencias/
    └── 📄 Azure Datalake Containers.png
    └── 📄 Azure resource manager proyecto.png
    └── 📄 ETL ejecucion.png    
├── 📂 prepamb/
    └── 📄 Preparacion_Ambiente       
├── 📂 proceso/
│   ├── 🐍 Ingest_customer_details           # Bronze layer
│   ├── 🐍 Ingest_ecommerce_sales            # Bronze Layer
│   ├── 🐍 Ingest_product_details            # Bronze Layer
│   ├── 🐍 Load                              # Golden Layer
│   ├── 🐍 Transform                         # Silver Layer
│   └── 🐍 Preparacion_Ambiente              # Create Schema, Tables, External location
├── 📂 reversion/
|   ├── 🐍 drop_tables                       # Eliminacion de Tablas
├── 📂 seguridad/
|   ├── 🐍 permisos                          # Sql Grant
├── 📂 dashboards/                           # Databricks Dashboards
|   ├── 📄 Dashboard_Ecommerce 
|   ├── 📄 Dashboard_1.png
|   ├── 📄 Dashboard_2.png
|   ├── 📄 Dashboard_3.png
└── 📄 README.md
```

---

## 🛠️ Tecnologías

<div align="center">

| Tecnología | Propósito |
|:----------:|:----------|
| ![Databricks](https://img.shields.io/badge/Azure_Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white) | Motor de procesamiento distribuido Spark |
| ![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=flat-square&logo=delta&logoColor=white) | Storage layer con ACID transactions |
| ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white) | Framework de transformación de datos |
| ![ADLS](https://img.shields.io/badge/ADLS_Gen2-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white) | Data Lake para almacenamiento persistente |
| ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) | Automatización CI/CD |
| ![Databricks Dashboards](https://img.shields.io/badge/Databricks Dashboards-F2C81?style=for-the-badge&logo=databricks&logoColor=black) |  Visualización |

</div>

---

## ⚙️ Requisitos Previos

- ☁️ Cuenta de Azure con acceso a Databricks
- 💻 Workspace de Databricks configurado
- 🖥️ Cluster activo (nombre: `ClusterSD`)
- 🐙 Cuenta de GitHub con permisos de administrador
- 📦 Azure Data Lake Storage Gen2 configurado

---


## 👤 Autor

<div align="center">

### Felipe Concha Rojas

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/felipe-concha-6288a941)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/felipeudp)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:felipe.cnch@gmail.com)

**Data Engineering** | **Azure Databricks** | **Delta Lake** | **CI/CD**

</div>

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**Proyecto**: Data Engineering - Arquitectura Medallion  
**Tecnología**: Azure Databricks + Delta Lake + CI/CD  
**Última actualización**: 2026


</div>
