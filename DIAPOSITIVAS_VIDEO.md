# 📊 DIAPOSITIVAS OPCIONALES PARA EL VIDEO
## (Si prefieres usar presentación en vez de mostrar archivos)

---

## DIAPOSITIVA 1: TÍTULO
```
┌─────────────────────────────────────────────────┐
│                                                 │
│     ANÁLISIS ESTADÍSTICO MULTIVARIADO          │
│                                                 │
│     Comparación de 4 Métodos de Reducción      │
│          de Dimensionalidad                     │
│                                                 │
│              [TU NOMBRE]                        │
│           Diciembre 2025                        │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 2: CONTEXTO
```
┌─────────────────────────────────────────────────┐
│  📊 DATOS ANALIZADOS                           │
│                                                 │
│  ✓ 620 observaciones                          │
│  ✓ 44 variables numéricas                     │
│  ✓ 2 archivos Excel originales                │
│                                                 │
│  🎯 OBJETIVO                                   │
│                                                 │
│  Comparar 4 técnicas estadísticas para         │
│  reducir complejidad y encontrar patrones      │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 3: MÉTODOS
```
┌─────────────────────────────────────────────────┐
│  🔬 MÉTODOS APLICADOS                          │
│                                                 │
│  1️⃣ ACP (PCA)                                  │
│     • Reducción matemática                     │
│     • Maximiza varianza                        │
│                                                 │
│  2️⃣ AFE                                        │
│     • Análisis factorial                       │
│     • Enfoque teórico                          │
│                                                 │
│  3️⃣ CLUSTERING                                 │
│     • K-means                                  │
│     • Agrupa observaciones                     │
│                                                 │
│  4️⃣ DISCRIMINANTE                              │
│     • LDA                                      │
│     • Clasificación supervisada                │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 4: RESULTADOS PCA
```
┌─────────────────────────────────────────────────┐
│  📈 ACP (PCA) - RESULTADOS                     │
│                                                 │
│  ✓ 11 componentes retenidos                   │
│    (Criterio Kaiser: λ > 1)                    │
│                                                 │
│  ✓ 55% varianza explicada                     │
│                                                 │
│  ✓ PC1 = 20.48% varianza                      │
│    (Variables A16R*)                           │
│                                                 │
│  [INSERTAR: scree_plot.png]                    │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 5: RESULTADOS AFE
```
┌─────────────────────────────────────────────────┐
│  📈 AFE - RESULTADOS                           │
│                                                 │
│  ✓ KMO = 0.898 (Muy bueno)                    │
│                                                 │
│  ✓ Test Bartlett: p < 0.001                   │
│    (Datos adecuados)                           │
│                                                 │
│  ✓ 11 factores identificados                  │
│                                                 │
│  ✓ Estructura factorial clara                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 6: RESULTADOS CLUSTERING
```
┌─────────────────────────────────────────────────┐
│  📈 CLUSTERING - RESULTADOS                    │
│                                                 │
│  ✓ 2 clusters óptimos                         │
│                                                 │
│  ✓ Distribución:                              │
│    • Cluster 0: 71.1% (441 obs)              │
│    • Cluster 1: 28.9% (179 obs)              │
│                                                 │
│  ✓ Silhouette = 0.176                         │
│    (Separación débil)                          │
│                                                 │
│  [INSERTAR: visualizacion_clusters.png]        │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 7: RESULTADOS DISCRIMINANTE
```
┌─────────────────────────────────────────────────┐
│  📈 DISCRIMINANTE - RESULTADOS                 │
│                                                 │
│  ✓ Exactitud: 60.22%                          │
│                                                 │
│  ✓ 3 clases predichas                         │
│    (Alto, Bajo, Medio)                         │
│                                                 │
│  ✓ Variables discriminantes:                  │
│    • responseID                                │
│    • Localidad                                 │
│    • A16R*                                     │
│                                                 │
│  [INSERTAR: matriz_confusion_lda.png]          │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 8: COMPARACIÓN
```
┌─────────────────────────────────────────────────┐
│  🔄 COMPARACIÓN DE MÉTODOS                     │
│                                                 │
│  Método      │ Mejor para...                   │
│  ───────────────────────────────────────────   │
│  PCA         │ Reducción técnica              │
│  AFE         │ Teoría/escalas                 │
│  Clustering  │ Segmentación                   │
│  Discriminan │ Clasificación                  │
│                                                 │
│  💡 No hay un método "mejor"                   │
│     Cada uno tiene su propósito                │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 9: CONCLUSIONES
```
┌─────────────────────────────────────────────────┐
│  🎯 CONCLUSIONES                               │
│                                                 │
│  1️⃣ Cada método tiene propósito específico    │
│                                                 │
│  2️⃣ IA ayudó con cálculos,                    │
│     humano con decisiones                      │
│                                                 │
│  3️⃣ Interpretación requiere                   │
│     pensamiento crítico                        │
│                                                 │
│  4️⃣ Combinación IA + humano                   │
│     es más poderosa                            │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 10: APRENDIZAJES
```
┌─────────────────────────────────────────────────┐
│  📚 LO QUE APRENDÍ                             │
│                                                 │
│  ✓ Diferencias entre métodos estadísticos     │
│                                                 │
│  ✓ Interpretación de métricas complejas       │
│                                                 │
│  ✓ Uso de Python para análisis estadístico    │
│                                                 │
│  ✓ Rol de IA vs pensamiento humano            │
│                                                 │
│  ✓ Importancia de la reflexión crítica        │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 11: HERRAMIENTAS
```
┌─────────────────────────────────────────────────┐
│  🛠️ HERRAMIENTAS UTILIZADAS                   │
│                                                 │
│  📊 Python 3.9                                 │
│  📊 scikit-learn (PCA, LDA, K-means)          │
│  📊 factor-analyzer (AFE)                     │
│  📊 pandas (manipulación datos)               │
│  📊 matplotlib/seaborn (visualización)        │
│                                                 │
│  📝 Archivos generados:                        │
│     • 15 tablas Excel                         │
│     • 8 gráficos profesionales                │
│     • 6 reportes detallados                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## DIAPOSITIVA 12: CIERRE
```
┌─────────────────────────────────────────────────┐
│                                                 │
│         "La IA automatiza cálculos,            │
│      el humano interpreta resultados"          │
│                                                 │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                 │
│              ¡GRACIAS!                          │
│                                                 │
│            [TU NOMBRE]                          │
│         Diciembre 2025                          │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 📝 NOTAS PARA CREAR DIAPOSITIVAS

### Opción 1: PowerPoint / Google Slides
1. Usa plantilla simple y profesional
2. Colores: Azul/Verde para estadísticas
3. Fuente: Arial o Calibri, tamaño 24-32
4. Incluye los gráficos PNG generados

### Opción 2: Canva
1. Busca plantilla "Presentación Estadística"
2. Copia el texto de cada diapositiva
3. Arrastra los gráficos PNG
4. Exporta como PDF o PPTX

### Opción 3: Markdown + Reveal.js
1. Usa el texto tal cual
2. Convierte a HTML con reveal.js
3. Presenta en navegador

---

## 🎨 SUGERENCIAS DE DISEÑO

### Colores Sugeridos:
- **Fondo:** Blanco o gris muy claro
- **Títulos:** Azul oscuro (#2C3E50)
- **Texto:** Gris oscuro (#34495E)
- **Acentos:** Verde (#27AE60) o Azul (#3498DB)

### Íconos:
- 📊 Para datos y gráficos
- 🔬 Para métodos científicos
- ✓ Para resultados positivos
- 💡 Para conclusiones
- 🎯 Para objetivos

### Formato:
- **Máximo 5-6 puntos por diapositiva**
- **Fuente grande** (mínimo 24pt)
- **Imágenes grandes** (ocupan 50%+ de slide)
- **Espacios en blanco** (no sobrecargar)

---

## ⏱️ TIMING CON DIAPOSITIVAS

| Diapositiva | Tiempo | Acción |
|-------------|--------|--------|
| 1 (Título) | 5 seg | Presentarse |
| 2 (Contexto) | 15 seg | Explicar datos |
| 3 (Métodos) | 40 seg | Explicar cada método |
| 4 (PCA) | 15 seg | Mostrar resultados |
| 5 (AFE) | 15 seg | Mostrar resultados |
| 6 (Clustering) | 15 seg | Mostrar resultados |
| 7 (Discriminante) | 15 seg | Mostrar resultados |
| 8 (Comparación) | 20 seg | Comparar métodos |
| 9 (Conclusiones) | 20 seg | Mensaje clave |
| 10 (Aprendizajes) | 15 seg | Reflexión |
| 11 (Herramientas) | Opcional | Si sobra tiempo |
| 12 (Cierre) | 5 seg | Despedirse |

**Total:** ~3 minutos

---

## 💡 TIPS FINALES

✅ **Menos es más** - No llenes las diapositivas
✅ **Visuales > Texto** - Usa los gráficos generados
✅ **Colores consistentes** - Mismo esquema en todas
✅ **Fuente legible** - Grande y clara
✅ **Practica transiciones** - Flujo natural

---

## 🚀 CREAR PRESENTACIÓN RÁPIDA

### En 10 minutos:

1. **Abre Google Slides** (o PowerPoint)
2. **Crea 10 diapositivas** (título + 9 contenido)
3. **Copia el texto** de este documento
4. **Inserta los gráficos** desde carpeta graficos/
5. **Ajusta formato** (fuente, colores)
6. **Practica una vez** cronometrando
7. **¡Graba!**

---

**Archivo:** DIAPOSITIVAS_VIDEO.md  
**Uso:** Opcional (alternativa a mostrar archivos directamente)  
**Ventaja:** Más estructurado y profesional  
**Desventaja:** Requiere tiempo de preparación
