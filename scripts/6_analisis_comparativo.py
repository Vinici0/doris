"""
Script 6: Análisis Comparativo
Compara los 4 métodos de reducción de dimensionalidad.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configuración
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def generar_analisis_comparativo(output_dir='../resultados'):
    """Genera un análisis comparativo completo de los 4 métodos"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    comparacion = []
    comparacion.append("=" * 100)
    comparacion.append("🔄 ANÁLISIS COMPARATIVO DE MÉTODOS DE REDUCCIÓN DE DIMENSIONALIDAD")
    comparacion.append("=" * 100)
    comparacion.append("")
    
    # Tabla comparativa
    comparacion.append("📊 TABLA COMPARATIVA DE MÉTODOS")
    comparacion.append("-" * 100)
    comparacion.append("")
    
    # Crear tabla
    tabla = {
        'Aspecto': [
            'Objetivo principal',
            'Tipo de método',
            'Reduce dimensiones',
            'Agrupa observaciones',
            'Variables de entrada',
            'Variables de salida',
            'Interpretabilidad',
            'Complejidad',
            'Sensibilidad a outliers',
            'Requiere variable dependiente'
        ],
        'ACP (PCA)': [
            'Maximizar varianza',
            'No supervisado',
            'Sí',
            'No',
            'Continuas',
            'Componentes principales',
            'Media',
            'Baja',
            'Alta',
            'No'
        ],
        'AFE': [
            'Identificar factores latentes',
            'No supervisado',
            'Sí',
            'No',
            'Continuas',
            'Factores latentes',
            'Alta',
            'Media',
            'Media',
            'No'
        ],
        'Cluster': [
            'Agrupar similares',
            'No supervisado',
            'No directamente',
            'Sí',
            'Continuas',
            'Grupos/clusters',
            'Alta',
            'Media',
            'Alta',
            'No'
        ],
        'Discriminante': [
            'Maximizar separación grupos',
            'Supervisado',
            'Sí',
            'Clasifica',
            'Continuas',
            'Funciones discriminantes',
            'Media',
            'Media',
            'Media',
            'Sí (categórica)'
        ]
    }
    
    df_tabla = pd.DataFrame(tabla)
    
    # Mostrar tabla
    comparacion.append(df_tabla.to_string(index=False))
    comparacion.append("")
    comparacion.append("")
    
    # Pregunta 1: ¿Qué método redujo mejor los datos?
    comparacion.append("1️⃣ ¿QUÉ MÉTODO REDUJO MEJOR LOS DATOS?")
    comparacion.append("-" * 100)
    comparacion.append("")
    comparacion.append("   📌 ACP (Análisis de Componentes Principales):")
    comparacion.append("      • Reduce dimensiones manteniendo máxima varianza")
    comparacion.append("      • Crea componentes ortogonales (no correlacionados)")
    comparacion.append("      • Bueno cuando el objetivo es reducir variables sin perder información")
    comparacion.append("      • Ejemplo: De 50 variables → 10 componentes que explican 90% varianza")
    comparacion.append("")
    comparacion.append("   📌 AFE (Análisis Factorial Exploratorio):")
    comparacion.append("      • Similar a PCA pero busca estructura factorial subyacente")
    comparacion.append("      • Asume que hay factores latentes que causan las correlaciones")
    comparacion.append("      • Mejor para teorización y construcción de escalas")
    comparacion.append("      • Ejemplo: Identificar 3 factores (ansiedad, depresión, estrés)")
    comparacion.append("")
    comparacion.append("   📌 Cluster:")
    comparacion.append("      • NO reduce dimensiones directamente")
    comparacion.append("      • Agrupa observaciones similares")
    comparacion.append("      • Útil para segmentación y perfiles")
    comparacion.append("      • Ejemplo: Identificar 4 tipos de clientes")
    comparacion.append("")
    comparacion.append("   📌 Discriminante:")
    comparacion.append("      • Reduce dimensiones maximizando separación entre grupos conocidos")
    comparacion.append("      • Requiere variable categórica de salida")
    comparacion.append("      • Útil para clasificación y predicción")
    comparacion.append("      • Ejemplo: Predecir diagnóstico basado en síntomas")
    comparacion.append("")
    comparacion.append("   ✅ CONCLUSIÓN:")
    comparacion.append("      • Para REDUCCIÓN PURA de datos: ACP es el mejor")
    comparacion.append("      • Para COMPRENSIÓN TEÓRICA: AFE es el mejor")
    comparacion.append("      • Para SEGMENTACIÓN: Cluster es el mejor")
    comparacion.append("      • Para CLASIFICACIÓN: Discriminante es el mejor")
    comparacion.append("")
    comparacion.append("")
    
    # Pregunta 2: ¿Qué método fue más fácil de interpretar?
    comparacion.append("2️⃣ ¿QUÉ MÉTODO FUE MÁS FÁCIL DE INTERPRETAR?")
    comparacion.append("-" * 100)
    comparacion.append("")
    comparacion.append("   🥇 MÁS FÁCIL: Cluster")
    comparacion.append("      • Los grupos son tangibles y directos")
    comparacion.append("      • Puedes describir características de cada grupo")
    comparacion.append("      • Ejemplo: 'Grupo 1 son personas jóvenes y saludables'")
    comparacion.append("")
    comparacion.append("   🥈 SEGUNDO: AFE")
    comparacion.append("      • Los factores tienen interpretación conceptual")
    comparacion.append("      • Las cargas altas indican relaciones claras")
    comparacion.append("      • Ejemplo: 'Factor 1 agrupa ítems de depresión'")
    comparacion.append("")
    comparacion.append("   🥉 TERCERO: Discriminante")
    comparacion.append("      • Las funciones discriminantes son menos intuitivas")
    comparacion.append("      • Pero los coeficientes muestran importancia de variables")
    comparacion.append("      • La exactitud es fácil de entender")
    comparacion.append("")
    comparacion.append("   🏅 CUARTO: ACP")
    comparacion.append("      • Los componentes principales son abstractos")
    comparacion.append("      • Difícil dar significado sustantivo a 'PC1' o 'PC2'")
    comparacion.append("      • Más útil para reducción que para interpretación")
    comparacion.append("")
    comparacion.append("")
    
    # Pregunta 3: ¿Qué método dio resultados más claros?
    comparacion.append("3️⃣ ¿QUÉ MÉTODO DIO RESULTADOS MÁS CLAROS?")
    comparacion.append("-" * 100)
    comparacion.append("")
    comparacion.append("   Depende del objetivo:")
    comparacion.append("")
    comparacion.append("   📊 Para visualización de patrones: CLUSTER")
    comparacion.append("      • Los gráficos de clusters son muy claros")
    comparacion.append("      • Fácil ver separación entre grupos")
    comparacion.append("")
    comparacion.append("   📊 Para validar escalas psicométricas: AFE")
    comparacion.append("      • Las cargas factoriales muestran qué ítems van juntos")
    comparacion.append("      • Comunalidades indican qué tan bien se explica cada variable")
    comparacion.append("")
    comparacion.append("   📊 Para predecir categorías: DISCRIMINANTE")
    comparacion.append("      • La exactitud es un resultado claro")
    comparacion.append("      • La matriz de confusión muestra aciertos/errores")
    comparacion.append("")
    comparacion.append("   📊 Para reducción técnica: ACP")
    comparacion.append("      • La varianza explicada es clara")
    comparacion.append("      • El scree plot muestra cuántos componentes retener")
    comparacion.append("")
    comparacion.append("")
    
    # Pregunta 4: Diferencias entre métodos
    comparacion.append("4️⃣ DIFERENCIAS PRINCIPALES ENTRE LOS 4 MÉTODOS")
    comparacion.append("-" * 100)
    comparacion.append("")
    comparacion.append("   🔵 ACP vs AFE:")
    comparacion.append("      • ACP: Enfoque puramente matemático (maximiza varianza)")
    comparacion.append("      • AFE: Enfoque teórico (busca causas latentes)")
    comparacion.append("      • ACP: Todos los componentes son ortogonales")
    comparacion.append("      • AFE: Puede permitir correlación entre factores (rotación oblicua)")
    comparacion.append("")
    comparacion.append("   🔵 ACP/AFE vs Cluster:")
    comparacion.append("      • ACP/AFE: Reducen VARIABLES (columnas)")
    comparacion.append("      • Cluster: Agrupa OBSERVACIONES (filas)")
    comparacion.append("      • ACP/AFE: Salida son puntuaciones/scores")
    comparacion.append("      • Cluster: Salida son etiquetas de grupo")
    comparacion.append("")
    comparacion.append("   🔵 Métodos no supervisados vs Discriminante:")
    comparacion.append("      • ACP/AFE/Cluster: No requieren variable dependiente")
    comparacion.append("      • Discriminante: REQUIERE una variable categórica conocida")
    comparacion.append("      • Discriminante es el único SUPERVISADO")
    comparacion.append("")
    comparacion.append("   🔵 Propósito final:")
    comparacion.append("      • ACP: Reducción de dimensionalidad sin pérdida de info")
    comparacion.append("      • AFE: Descubrir estructura factorial teórica")
    comparacion.append("      • Cluster: Segmentación y tipologías")
    comparacion.append("      • Discriminante: Clasificación y predicción")
    comparacion.append("")
    comparacion.append("")
    
    # Cuándo usar cada método
    comparacion.append("📋 GUÍA DE USO: ¿CUÁNDO USAR CADA MÉTODO?")
    comparacion.append("-" * 100)
    comparacion.append("")
    comparacion.append("   ✅ Usa ACP cuando:")
    comparacion.append("      • Tienes muchas variables correlacionadas")
    comparacion.append("      • Quieres reducir dimensiones manteniendo información")
    comparacion.append("      • Necesitas variables no correlacionadas para regresión")
    comparacion.append("      • Quieres visualizar datos multidimensionales")
    comparacion.append("")
    comparacion.append("   ✅ Usa AFE cuando:")
    comparacion.append("      • Estás desarrollando o validando cuestionarios")
    comparacion.append("      • Quieres entender estructura latente de datos")
    comparacion.append("      • Buscas constructos teóricos subyacentes")
    comparacion.append("      • Trabajas en psicología, educación, ciencias sociales")
    comparacion.append("")
    comparacion.append("   ✅ Usa Cluster cuando:")
    comparacion.append("      • Quieres segmentar clientes/pacientes/estudiantes")
    comparacion.append("      • Buscas patrones naturales de agrupamiento")
    comparacion.append("      • Necesitas crear tipologías")
    comparacion.append("      • Quieres personalizar intervenciones por grupo")
    comparacion.append("")
    comparacion.append("   ✅ Usa Discriminante cuando:")
    comparacion.append("      • Tienes grupos conocidos y quieres predecir membresía")
    comparacion.append("      • Quieres saber qué variables mejor distinguen grupos")
    comparacion.append("      • Necesitas clasificar nuevas observaciones")
    comparacion.append("      • Tienes variable categórica de salida")
    comparacion.append("")
    comparacion.append("")
    comparacion.append("=" * 100)
    
    # Guardar tabla
    path_tabla = Path(output_dir) / 'tabla_comparativa.xlsx'
    df_tabla.to_excel(path_tabla, index=False)
    print(f"📊 Tabla comparativa guardada: {path_tabla}")
    
    # Guardar análisis completo
    comparacion_text = "\n".join(comparacion)
    print("\n" + comparacion_text)
    
    path = Path(output_dir) / 'analisis_comparativo.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(comparacion_text)
    
    print(f"\n💾 Análisis comparativo guardado: {path}")
    
    return df_tabla

def crear_grafico_comparativo(output_dir='../graficos'):
    """Crea gráfico visual comparando los métodos"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Datos para el gráfico
    metodos = ['ACP', 'AFE', 'Cluster', 'Discriminante']
    
    # Puntuaciones en diferentes aspectos (escala 1-5)
    interpretabilidad = [2, 4, 5, 3]
    reduccion = [5, 4, 2, 4]
    complejidad_uso = [4, 3, 4, 3]  # Invertido: mayor es más fácil
    aplicabilidad = [4, 3, 4, 3]
    
    # Crear gráfico de radar
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico de barras
    x = range(len(metodos))
    width = 0.2
    
    axes[0].bar([i - 1.5*width for i in x], interpretabilidad, width, label='Interpretabilidad', alpha=0.8)
    axes[0].bar([i - 0.5*width for i in x], reduccion, width, label='Capacidad reducción', alpha=0.8)
    axes[0].bar([i + 0.5*width for i in x], complejidad_uso, width, label='Facilidad uso', alpha=0.8)
    axes[0].bar([i + 1.5*width for i in x], aplicabilidad, width, label='Aplicabilidad', alpha=0.8)
    
    axes[0].set_ylabel('Puntuación (1-5)', fontsize=11)
    axes[0].set_title('Comparación de Métodos', fontsize=13, fontweight='bold')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(metodos)
    axes[0].legend()
    axes[0].set_ylim(0, 6)
    axes[0].grid(axis='y', alpha=0.3)
    
    # Tabla resumen
    axes[1].axis('off')
    tabla_data = [
        ['Método', 'Mejor para...'],
        ['ACP', 'Reducción técnica'],
        ['AFE', 'Teoría/escalas'],
        ['Cluster', 'Segmentación'],
        ['Discriminante', 'Clasificación']
    ]
    
    tabla = axes[1].table(cellText=tabla_data, loc='center', cellLoc='left',
                          colWidths=[0.3, 0.7])
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2)
    
    # Estilo de la tabla
    for i in range(len(tabla_data)):
        if i == 0:
            tabla[(i, 0)].set_facecolor('#4CAF50')
            tabla[(i, 1)].set_facecolor('#4CAF50')
            tabla[(i, 0)].set_text_props(weight='bold', color='white')
            tabla[(i, 1)].set_text_props(weight='bold', color='white')
        else:
            tabla[(i, 0)].set_facecolor('#E8F5E9')
            tabla[(i, 1)].set_facecolor('#F5F5F5')
    
    plt.tight_layout()
    
    path = Path(output_dir) / 'comparacion_metodos.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Gráfico comparativo guardado: {path}")
    plt.close()

def main():
    """Función principal"""
    print("=" * 100)
    print("🔄 ANÁLISIS 3: ANÁLISIS COMPARATIVO DE MÉTODOS")
    print("=" * 100)
    
    # Generar análisis textual
    df_tabla = generar_analisis_comparativo()
    
    # Crear gráfico comparativo
    crear_grafico_comparativo()
    
    print("\n✅ ¡Análisis comparativo completado!")
    print("\n📌 Respuestas a las preguntas:")
    print("   1. ¿Qué método redujo mejor? → Depende del objetivo (ver informe)")
    print("   2. ¿Más fácil de interpretar? → Cluster > AFE > Discriminante > ACP")
    print("   3. ¿Resultados más claros? → Depende del objetivo (ver informe)")
    print("   4. ¿Diferencias? → Ver análisis comparativo completo")
    
    return df_tabla

if __name__ == "__main__":
    df_tabla = main()
