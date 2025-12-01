# 📊 Proyecto de Análisis Estadístico Multivariado

Sistema completo de análisis estadístico en Python que implementa 4 técnicas de reducción de dimensionalidad y análisis comparativo.

## 📁 Estructura del Proyecto

```
doris/
├── BASE_ETIQUETAS.xlsx          # Archivo de datos con etiquetas
├── BASE_NOMBRES_Y_VALORES.xlsx  # Archivo de datos con valores codificados
├── requirements.txt             # Dependencias Python
├── venv/                        # Entorno virtual (generado)
├── README.md                    # Este archivo
│
├── scripts/                     # Scripts de análisis
│   ├── 1_hoja_codificacion.py           # Genera tabla de codificación
│   ├── 2_analisis_pca.py                # Análisis de Componentes Principales
│   ├── 3_analisis_afe.py                # Análisis Factorial Exploratorio
│   ├── 4_analisis_clustering.py         # Análisis de Clustering (K-means)
│   ├── 5_analisis_discriminante.py      # Análisis Discriminante (LDA)
│   ├── 6_analisis_comparativo.py        # Comparación de métodos
│   ├── 7_reflexion_critica.py           # Plantilla de reflexión
│   └── main.py                          # Script principal (ejecuta todo)
│
├── resultados/                  # Resultados generados
│   ├── *.xlsx                   # Tablas de resultados
│   └── *.txt                    # Reportes textuales
│
└── graficos/                    # Gráficos generados
    └── *.png                    # Visualizaciones
```

## 🚀 Instalación y Configuración

### Paso 1: Verificar Python

Asegúrate de tener Python 3.8 o superior:

```bash
python3 --version
```

### Paso 2: El entorno virtual ya está creado

El entorno virtual `venv` ya fue creado y las dependencias instaladas.

### Paso 3: Activar el entorno virtual

**En macOS/Linux:**
```bash
cd /Users/vinicioborja/Downloads/doris
source venv/bin/activate
```

**En Windows:**
```bash
cd C:\ruta\a\doris
venv\Scripts\activate
```

Verás `(venv)` al inicio de tu línea de comandos cuando esté activo.

## ▶️ Cómo Ejecutar

### Opción 1: Ejecutar TODO el análisis (Recomendado)

```bash
cd scripts
python main.py
```

Este script ejecuta automáticamente los 7 análisis en secuencia:
1. Hoja de Codificación
2. ACP (PCA)
3. AFE
4. Clustering
5. Discriminante
6. Comparativo
7. Reflexión

⏱️ **Tiempo estimado:** 2-5 minutos

### Opción 2: Ejecutar análisis individuales

Si quieres ejecutar solo un análisis específico:

```bash
cd scripts

# Hoja de codificación
python 1_hoja_codificacion.py

# Análisis de Componentes Principales
python 2_analisis_pca.py

# Análisis Factorial Exploratorio
python 3_analisis_afe.py

# Análisis de Clustering
python 4_analisis_clustering.py

# Análisis Discriminante
python 5_analisis_discriminante.py

# Análisis Comparativo
python 6_analisis_comparativo.py

# Plantilla de Reflexión
python 7_reflexion_critica.py
```

## 📊 Análisis Incluidos

### 1️⃣ Hoja de Codificación (OBLIGATORIA)

**¿Qué hace?**
- Compara `BASE_ETIQUETAS.xlsx` con `BASE_NOMBRES_Y_VALORES.xlsx`
- Determina cómo está codificada cada variable
- Genera tabla con mínimo 10 variables

**Salidas:**
- `resultados/tabla_codificacion.xlsx`
- `resultados/tabla_codificacion.csv`

**Ejemplo de resultado:**
| Variable | Descripción | Codificación |
|----------|-------------|--------------|
| A1 | Sexo | 1 = Hombre / 2 = Mujer |
| A2 | Embarazo | 1 = Sí / 2 = No |

### 2️⃣ Análisis de Componentes Principales (ACP/PCA)

**¿Qué hace?**
- Reduce dimensionalidad maximizando varianza
- Calcula componentes principales ortogonales
- Determina cuántos componentes retener

**Preguntas que responde:**
- ✅ ¿Cuántos componentes retienes?
- ✅ ¿Qué % de varianza explican?
- ✅ ¿Qué ítems cargan más en cada componente?

**Salidas:**
- `graficos/scree_plot.png` - Gráfico de sedimentación
- `resultados/tabla_autovalores.xlsx` - Autovalores y varianza
- `resultados/tabla_cargas_factoriales.xlsx` - Cargas por componente
- `graficos/mapa_calor_cargas.png` - Mapa de calor
- `resultados/reporte_pca.txt` - Reporte completo

### 3️⃣ Análisis Factorial Exploratorio (AFE)

**¿Qué hace?**
- Identifica factores latentes subyacentes
- Evalúa adecuación muestral (KMO, Bartlett)
- Compara con PCA

**Preguntas que responde:**
- ✅ Número de factores elegido
- ✅ Cargas factoriales evaluadas
- ✅ Comparación con PCA
- ✅ Coherencia de factores

**Salidas:**
- `graficos/scree_plot_afe.png`
- `resultados/tabla_cargas_afe.xlsx`
- `graficos/mapa_calor_afe.png`
- `resultados/reporte_afe.txt`
- `resultados/comparacion_afe_pca.txt`

### 4️⃣ Análisis de Clustering (K-means)

**¿Qué hace?**
- Agrupa observaciones similares
- Usa método del codo para elegir K óptimo
- Describe cada grupo identificado

**Preguntas que responde:**
- ✅ Número óptimo de clusters
- ✅ Descripción de cada grupo
- ✅ Qué tipo de personas hay en cada cluster

**Salidas:**
- `graficos/metricas_clustering.png` - Método del codo y métricas
- `resultados/estadisticas_clusters.xlsx` - Estadísticas por cluster
- `resultados/descripcion_clusters.xlsx` - Descripción de grupos
- `graficos/visualizacion_clusters.png` - Visualización 2D
- `resultados/interpretacion_clusters.txt` - Interpretación
- `resultados/reporte_clustering.txt` - Reporte completo

### 5️⃣ Análisis Discriminante (LDA)

**¿Qué hace?**
- Clasifica observaciones en grupos conocidos
- Evalúa qué variables discriminan mejor
- Calcula exactitud de clasificación

**Preguntas que responde:**
- ✅ Variable categórica seleccionada
- ✅ Exactitud del modelo
- ✅ Matriz de confusión
- ✅ Variables más discriminantes

**Salidas:**
- `graficos/matriz_confusion_lda.png`
- `graficos/espacio_discriminante.png`
- `resultados/coeficientes_discriminantes.xlsx`
- `resultados/reporte_discriminante.txt`

### 6️⃣ Análisis Comparativo

**¿Qué hace?**
- Compara los 4 métodos utilizados
- Evalúa fortalezas y debilidades
- Guía para elegir método apropiado

**Preguntas que responde:**
- ✅ ¿Qué método redujo mejor los datos?
- ✅ ¿Qué método fue más fácil de interpretar?
- ✅ ¿Qué método dio resultados más claros?
- ✅ ¿Qué diferencias hay entre métodos?

**Salidas:**
- `resultados/tabla_comparativa.xlsx`
- `graficos/comparacion_metodos.png`
- `resultados/analisis_comparativo.txt`

### 7️⃣ Reflexión Crítica

**¿Qué hace?**
- Genera plantilla para reflexión PERSONAL
- Guía para reflexionar sobre el proceso
- Debe ser completada por TI

**Preguntas que debes responder:**
- ✅ ¿Qué fue lo más difícil?
- ✅ ¿Qué decisiones tomaste tú?
- ✅ ¿En qué ayudó la IA?
- ✅ ¿Qué NO puede automatizar la IA?
- ✅ ¿Qué aprendiste?

**Salida:**
- `resultados/plantilla_reflexion_critica.txt` - ⚠️ **DEBES COMPLETARLA TÚ**

## 📝 Dependencias

El proyecto usa las siguientes librerías Python:

- **pandas** - Manipulación de datos
- **numpy** - Cálculos numéricos
- **matplotlib** - Visualización
- **seaborn** - Visualización avanzada
- **scikit-learn** - Algoritmos de ML (PCA, LDA, K-means)
- **factor-analyzer** - Análisis factorial
- **openpyxl** - Leer/escribir Excel
- **scipy** - Funciones científicas

Todas ya están instaladas en el entorno virtual.

## 🎯 División de Trabajo: IA vs Humano

### 🤖 Lo que HIZO la IA:

✅ Generar código Python  
✅ Implementar algoritmos estadísticos  
✅ Calcular métricas numéricas  
✅ Crear gráficos y tablas  
✅ Estructurar proyecto  
✅ Generar plantillas  

### 👤 Lo que DEBES HACER TÚ:

✅ **Ejecutar** los scripts  
✅ **Revisar** los resultados  
✅ **INTERPRETAR** los números (darles significado)  
✅ **DECIDIR** número de componentes/factores/clusters  
✅ **NOMBRAR** componentes/factores/clusters  
✅ **EVALUAR** coherencia con teoría  
✅ **CRITICAR** limitaciones  
✅ **REDACTAR** el informe final  
✅ **REFLEXIONAR** sobre el proceso  

## 📋 Checklist del Proyecto

### ✅ Requisitos del Trabajo

- [x] Hoja de codificación con mínimo 10 variables
- [x] ACP: Componentes retenidos, % varianza, cargas
- [x] ACP: Scree plot, tabla autovalores
- [x] AFE: Número de factores, cargas, comparación con PCA
- [x] AFE: Coherencia de factores explicada
- [x] Cluster: Método del codo, número óptimo
- [x] Cluster: Descripción de grupos
- [x] Cluster: Interpretación (qué personas en cada grupo)
- [x] Discriminante: Variable categórica, exactitud, matriz confusión
- [x] Comparación: Qué método redujo mejor
- [x] Comparación: Qué método más fácil interpretar
- [x] Comparación: Qué método resultados más claros
- [x] Comparación: Diferencias entre métodos
- [ ] Reflexión crítica completada ⚠️ **PENDIENTE POR TI**

### ✅ Archivos para el Informe

**Tablas Excel (incluir en informe):**
- [ ] `tabla_codificacion.xlsx`
- [ ] `tabla_autovalores.xlsx`
- [ ] `tabla_cargas_factoriales.xlsx`
- [ ] `tabla_cargas_afe.xlsx`
- [ ] `descripcion_clusters.xlsx`
- [ ] `coeficientes_discriminantes.xlsx`
- [ ] `tabla_comparativa.xlsx`

**Gráficos (incluir en informe):**
- [ ] `scree_plot.png`
- [ ] `mapa_calor_cargas.png`
- [ ] `scree_plot_afe.png`
- [ ] `mapa_calor_afe.png`
- [ ] `metricas_clustering.png`
- [ ] `visualizacion_clusters.png`
- [ ] `matriz_confusion_lda.png`
- [ ] `comparacion_metodos.png`

**Reportes de texto (usar para redactar):**
- [ ] `reporte_pca.txt`
- [ ] `reporte_afe.txt`
- [ ] `reporte_clustering.txt`
- [ ] `reporte_discriminante.txt`
- [ ] `analisis_comparativo.txt`
- [ ] `plantilla_reflexion_critica.txt` ⚠️ **COMPLETAR**

## 🆘 Solución de Problemas

### Problema: "ModuleNotFoundError"

**Solución:**
```bash
source venv/bin/activate  # Activar entorno
pip install -r requirements.txt  # Reinstalar dependencias
```

### Problema: "FileNotFoundError" al buscar Excel

**Solución:**
- Verifica que `BASE_ETIQUETAS.xlsx` y `BASE_NOMBRES_Y_VALORES.xlsx` estén en la carpeta raíz
- Los scripts deben ejecutarse desde la carpeta `scripts/`

### Problema: Errores en un análisis específico

**Solución:**
- Revisa los datos de entrada
- Ejecuta análisis individuales para identificar el problema
- Verifica que tengas suficientes datos numéricos

### Problema: No se generan archivos

**Solución:**
- Verifica permisos de escritura en las carpetas
- Las carpetas `resultados/` y `graficos/` se crean automáticamente

## 📚 Recursos Adicionales

### Teoría Estadística

- **PCA:** Jolliffe, I.T. (2002). Principal Component Analysis.
- **AFE:** Fabrigar & Wegener (2012). Exploratory Factor Analysis.
- **Clustering:** Kaufman & Rousseeuw (2005). Finding Groups in Data.
- **LDA:** Hastie et al. (2009). The Elements of Statistical Learning.

### Python y Análisis

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Factor Analyzer](https://factor-analyzer.readthedocs.io/)

## 💡 Consejos para el Informe

1. **Introducción:** Explica el objetivo y los datos
2. **Metodología:** Describe cada método brevemente
3. **Resultados:** Presenta tablas y gráficos con interpretación
4. **Comparación:** Usa el análisis comparativo generado
5. **Reflexión:** Incluye tu reflexión crítica personal
6. **Conclusiones:** Resume aprendizajes y limitaciones

## ⚠️ IMPORTANTE

- **NO copies los reportes generados textualmente** - Úsalos como guía
- **INTERPRETA los resultados** - No solo presentes números
- **COMPLETA la reflexión crítica** - Es personal, no puede ser automatizada
- **VERIFICA los resultados** - Asegúrate de que tengan sentido
- **CITA apropiadamente** - Menciona el uso de herramientas de IA si es requerido

## 📞 Soporte

Si tienes problemas:
1. Revisa este README
2. Lee los mensajes de error cuidadosamente
3. Verifica que el entorno virtual esté activado
4. Consulta con tu profesor si persisten los problemas

## 📄 Licencia

Este proyecto es para uso académico.

---

**¡Éxito en tu proyecto! 🎓**

Recuerda: La IA es una herramienta poderosa, pero TÚ eres el analista que da sentido a los datos.
