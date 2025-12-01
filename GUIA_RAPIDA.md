# 🚀 GUÍA RÁPIDA DE USO

## ⚡ Inicio Rápido (3 pasos)

### 1. Activar el entorno virtual

```bash
cd /Users/vinicioborja/Downloads/doris
source venv/bin/activate
```

### 2. Ejecutar el análisis completo

```bash
cd scripts
python main.py
```

Presiona ENTER cuando te lo pida y espera 2-5 minutos.

### 3. Revisar resultados

Los resultados están en:
- **resultados/** → Tablas Excel y reportes de texto
- **graficos/** → Gráficos PNG para tu informe

---

## 📊 ¿Qué se generó?

### ✅ Análisis Completados

| # | Análisis | Archivos Principales |
|---|----------|---------------------|
| 1️⃣ | **Hoja de Codificación** | `tabla_codificacion.xlsx` |
| 2️⃣ | **ACP (PCA)** | `reporte_pca.txt`, `scree_plot.png`, `tabla_autovalores.xlsx` |
| 3️⃣ | **AFE** | `reporte_afe.txt`, `tabla_cargas_afe.xlsx`, `scree_plot_afe.png` |
| 4️⃣ | **Clustering** | `reporte_clustering.txt`, `visualizacion_clusters.png`, `metricas_clustering.png` |
| 5️⃣ | **Discriminante** | `reporte_discriminante.txt`, `matriz_confusion_lda.png` |
| 6️⃣ | **Comparativo** | `analisis_comparativo.txt`, `comparacion_metodos.png` |
| 7️⃣ | **Reflexión** | `plantilla_reflexion_critica.txt` ⚠️ **COMPLETAR** |

---

## 📋 Checklist para tu Informe

### Sección 1: Hoja de Codificación ✅

- [ ] Incluir tabla de codificación (mínimo 10 variables)
- [ ] Archivo: `tabla_codificacion.xlsx`

### Sección 2A: ACP (Análisis de Componentes Principales) ✅

**Preguntas a responder:**
- [ ] ¿Cuántos componentes retienes? → Ver `reporte_pca.txt`
- [ ] ¿Qué % de varianza explican? → Ver `reporte_pca.txt`
- [ ] ¿Qué ítems cargan más? → Ver `tabla_cargas_factoriales.xlsx`

**Incluir en informe:**
- [ ] `scree_plot.png`
- [ ] `tabla_autovalores.xlsx`
- [ ] `mapa_calor_cargas.png`

### Sección 2B: AFE (Análisis Factorial Exploratorio) ✅

**Preguntas a responder:**
- [ ] Número de factores elegido → Ver `reporte_afe.txt`
- [ ] Cargas factoriales evaluadas → Ver `tabla_cargas_afe.xlsx`
- [ ] Comparación con PCA → Ver `comparacion_afe_pca.txt`
- [ ] ¿Son coherentes los factores? → Interpretar tú

**Incluir en informe:**
- [ ] `scree_plot_afe.png`
- [ ] `tabla_cargas_afe.xlsx`
- [ ] `mapa_calor_afe.png`

### Sección 2C: Clustering ✅

**Preguntas a responder:**
- [ ] Número de clusters probados → Ver `metricas_clustering.png`
- [ ] Número óptimo elegido → Ver `reporte_clustering.txt`
- [ ] Descripción de cada grupo → Ver `descripcion_clusters.xlsx`
- [ ] ¿Qué tipo de personas? → Ver `interpretacion_clusters.txt` y completar tú

**Incluir en informe:**
- [ ] `metricas_clustering.png` (método del codo)
- [ ] `visualizacion_clusters.png`
- [ ] `descripcion_clusters.xlsx`

### Sección 2D: Análisis Discriminante ✅

**Preguntas a responder:**
- [ ] Variable categórica usada → Ver `reporte_discriminante.txt`
- [ ] Exactitud del modelo → Ver `reporte_discriminante.txt`
- [ ] Variables más discriminantes → Ver `coeficientes_discriminantes.xlsx`

**Incluir en informe:**
- [ ] `matriz_confusion_lda.png`
- [ ] `espacio_discriminante.png`
- [ ] `coeficientes_discriminantes.xlsx`

### Sección 3: Análisis Comparativo ✅

**Preguntas a responder:**
- [ ] ¿Qué método redujo mejor? → Ver `analisis_comparativo.txt`
- [ ] ¿Más fácil de interpretar? → Ver `analisis_comparativo.txt`
- [ ] ¿Resultados más claros? → Ver `analisis_comparativo.txt`
- [ ] ¿Diferencias entre métodos? → Ver `analisis_comparativo.txt`

**Incluir en informe:**
- [ ] `tabla_comparativa.xlsx`
- [ ] `comparacion_metodos.png`

### Sección 4: Reflexión Crítica ⚠️

**⚠️ IMPORTANTE: Debes completar esto TÚ MISMO**

- [ ] Abrir: `plantilla_reflexion_critica.txt`
- [ ] Responder: ¿Qué fue lo más difícil?
- [ ] Responder: ¿Qué decisiones tomaste?
- [ ] Responder: ¿En qué ayudó la IA?
- [ ] Responder: ¿Qué NO puede automatizar la IA?
- [ ] Responder: ¿Qué aprendiste?

---

## 🎯 Respuestas Rápidas (de los reportes)

### ACP
- **Componentes retenidos:** 11 (criterio Kaiser)
- **Varianza explicada:** PC1-PC11 = ~55%
- **Interpretación:** Ver cargas en `tabla_cargas_factoriales.xlsx`

### AFE
- **Factores:** 11 factores
- **KMO:** 0.898 (Muy bueno)
- **Test Bartlett:** p < 0.001 (Adecuado)

### Clustering
- **Clusters óptimos:** 2 grupos
- **Tamaños:** Cluster 0 (71.1%), Cluster 1 (28.9%)
- **Calidad:** Silhouette = 0.176 (débil, podrías probar con 3-4 clusters)

### Discriminante
- **Variable:** Grupo_Artificial (creada automáticamente)
- **Exactitud:** 60.22%
- **Clases:** 3 (Alto, Bajo, Medio)

---

## 💡 Tips para el Informe

### ✅ HACER:
- **Usa tus propias palabras** para interpretar
- **Incluye todos los gráficos** y explícalos
- **Cita las métricas** de los reportes
- **Da significado** a los componentes/factores/clusters
- **Completa la reflexión** con honestidad

### ❌ NO HACER:
- No copies los reportes textualmente
- No incluyas resultados sin interpretación
- No ignores la reflexión crítica
- No presentes gráficos sin explicar qué muestran

---

## 🔧 Si Necesitas Re-ejecutar

### Ejecutar solo un análisis específico:

```bash
cd scripts

# Solo codificación
python 1_hoja_codificacion.py

# Solo PCA
python 2_analisis_pca.py

# Solo AFE
python 3_analisis_afe.py

# Solo Clustering
python 4_analisis_clustering.py

# Solo Discriminante
python 5_analisis_discriminante.py

# Solo Comparativo
python 6_analisis_comparativo.py

# Solo Reflexión
python 7_reflexion_critica.py
```

---

## 📞 ¿Problemas?

1. **"ModuleNotFoundError"** → `source venv/bin/activate`
2. **"FileNotFoundError"** → Verifica que los archivos .xlsx estén en la carpeta raíz
3. **Gráficos no se ven** → Están en carpeta `graficos/`, ábrelos con visor de imágenes
4. **Excel no abre** → Verifica que tengas Excel, LibreOffice, o Google Sheets

---

## 🎓 ¡Éxito!

Ahora tienes todo lo necesario para tu informe:
- ✅ 15 archivos Excel con resultados
- ✅ 8 gráficos profesionales
- ✅ 6 reportes detallados
- ✅ 1 plantilla de reflexión (complétala tú)

**Recuerda:** La IA hizo los cálculos, TÚ eres quien interpreta y da sentido a los datos.

---

**Creado con:** Python, scikit-learn, pandas, matplotlib, seaborn, factor-analyzer  
**Fecha:** Diciembre 2025
