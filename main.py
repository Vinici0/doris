"""
SCRIPT PRINCIPAL - Ejecuta todos los análisis
Este script ejecuta los 7 análisis en secuencia.
"""

import sys
import os
from pathlib import Path
import importlib.util

# Añadir el directorio de scripts al path
sys.path.insert(0, str(Path(__file__).parent))

def print_header(titulo, emoji="🔬"):
    """Imprime un encabezado bonito"""
    print("\n" + "=" * 100)
    print(f"{emoji} {titulo}")
    print("=" * 100 + "\n")

def cargar_modulo(nombre_archivo):
    """Carga un módulo Python dinámicamente"""
    ruta = Path(__file__).parent / nombre_archivo
    spec = importlib.util.spec_from_file_location(nombre_archivo[:-3], ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

def main():
    """Ejecuta todos los análisis en secuencia"""
    
    print_header("SISTEMA DE ANÁLISIS ESTADÍSTICO MULTIVARIADO", "🚀")
    print("Este script ejecutará 7 análisis completos:")
    print("   1️⃣  Hoja de Codificación")
    print("   2️⃣  Análisis de Componentes Principales (ACP)")
    print("   3️⃣  Análisis Factorial Exploratorio (AFE)")
    print("   4️⃣  Análisis de Clustering")
    print("   5️⃣  Análisis Discriminante")
    print("   6️⃣  Análisis Comparativo")
    print("   7️⃣  Plantilla de Reflexión Crítica")
    print("\n⏱️  Tiempo estimado: 2-5 minutos\n")
    
    input("Presiona ENTER para comenzar...")
    
    try:
        # ==========================================
        # 1️⃣ HOJA DE CODIFICACIÓN
        # ==========================================
        print_header("1/7 - HOJA DE CODIFICACIÓN", "1️⃣")
        try:
            mod1 = cargar_modulo("1_hoja_codificacion.py")
            df_codificacion = mod1.main()
            print("✅ Completado: Hoja de codificación")
        except Exception as e:
            print(f"❌ Error en hoja de codificación: {e}")
            print("Continuando con el siguiente análisis...")
        
        # ==========================================
        # 2️⃣ ANÁLISIS DE COMPONENTES PRINCIPALES
        # ==========================================
        print_header("2/7 - ANÁLISIS DE COMPONENTES PRINCIPALES (ACP)", "2️⃣")
        try:
            mod2 = cargar_modulo("2_analisis_pca.py")
            pca, componentes, df_cargas_pca = mod2.main()
            print("✅ Completado: ACP")
        except Exception as e:
            print(f"❌ Error en ACP: {e}")
            print("Continuando con el siguiente análisis...")
        
        # ==========================================
        # 3️⃣ ANÁLISIS FACTORIAL EXPLORATORIO
        # ==========================================
        print_header("3/7 - ANÁLISIS FACTORIAL EXPLORATORIO (AFE)", "3️⃣")
        try:
            mod3 = cargar_modulo("3_analisis_afe.py")
            fa, df_loadings = mod3.main()
            print("✅ Completado: AFE")
        except Exception as e:
            print(f"❌ Error en AFE: {e}")
            print("Continuando con el siguiente análisis...")
        
        # ==========================================
        # 4️⃣ ANÁLISIS DE CLUSTERING
        # ==========================================
        print_header("4/7 - ANÁLISIS DE CLUSTERING", "4️⃣")
        try:
            mod4 = cargar_modulo("4_analisis_clustering.py")
            kmeans, labels, df_clusters = mod4.main()
            print("✅ Completado: Clustering")
        except Exception as e:
            print(f"❌ Error en Clustering: {e}")
            print("Continuando con el siguiente análisis...")
        
        # ==========================================
        # 5️⃣ ANÁLISIS DISCRIMINANTE
        # ==========================================
        print_header("5/7 - ANÁLISIS DISCRIMINANTE", "5️⃣")
        try:
            mod5 = cargar_modulo("5_analisis_discriminante.py")
            lda, accuracy, cm = mod5.main()
            print("✅ Completado: Análisis Discriminante")
        except Exception as e:
            print(f"❌ Error en Discriminante: {e}")
            print("Continuando con el siguiente análisis...")
        
        # ==========================================
        # 6️⃣ ANÁLISIS COMPARATIVO
        # ==========================================
        print_header("6/7 - ANÁLISIS COMPARATIVO", "6️⃣")
        try:
            mod6 = cargar_modulo("6_analisis_comparativo.py")
            df_comparacion = mod6.main()
            print("✅ Completado: Análisis Comparativo")
        except Exception as e:
            print(f"❌ Error en Comparativo: {e}")
            print("Continuando con el siguiente análisis...")
        
        # ==========================================
        # 7️⃣ REFLEXIÓN CRÍTICA
        # ==========================================
        print_header("7/7 - PLANTILLA DE REFLEXIÓN CRÍTICA", "7️⃣")
        try:
            mod7 = cargar_modulo("7_reflexion_critica.py")
            mod7.main()
            print("✅ Completado: Plantilla de Reflexión")
        except Exception as e:
            print(f"❌ Error en Reflexión: {e}")
        
        # ==========================================
        # RESUMEN FINAL
        # ==========================================
        print_header("ANÁLISIS COMPLETADO", "🎉")
        
        print("📁 ARCHIVOS GENERADOS:")
        print("\n📊 Carpeta 'resultados/':")
        print("   • tabla_codificacion.xlsx - Codificación de variables")
        print("   • tabla_autovalores.xlsx - Autovalores del PCA")
        print("   • tabla_cargas_factoriales.xlsx - Cargas del PCA")
        print("   • tabla_cargas_afe.xlsx - Cargas del AFE")
        print("   • estadisticas_clusters.xlsx - Estadísticas por cluster")
        print("   • descripcion_clusters.xlsx - Descripción de clusters")
        print("   • coeficientes_discriminantes.xlsx - Coeficientes LDA")
        print("   • tabla_comparativa.xlsx - Tabla comparativa de métodos")
        print("   • reporte_pca.txt - Reporte completo PCA")
        print("   • reporte_afe.txt - Reporte completo AFE")
        print("   • reporte_clustering.txt - Reporte completo Clustering")
        print("   • reporte_discriminante.txt - Reporte completo LDA")
        print("   • analisis_comparativo.txt - Análisis comparativo")
        print("   • plantilla_reflexion_critica.txt - Para completar TÚ")
        
        print("\n📈 Carpeta 'graficos/':")
        print("   • scree_plot.png - Gráfico de sedimentación PCA")
        print("   • mapa_calor_cargas.png - Mapa de calor PCA")
        print("   • scree_plot_afe.png - Gráfico de sedimentación AFE")
        print("   • mapa_calor_afe.png - Mapa de calor AFE")
        print("   • metricas_clustering.png - Métricas de clustering")
        print("   • visualizacion_clusters.png - Visualización clusters")
        print("   • matriz_confusion_lda.png - Matriz de confusión")
        print("   • espacio_discriminante.png - Visualización LDA")
        print("   • comparacion_metodos.png - Comparación visual")
        
        print("\n" + "=" * 100)
        print("📋 PRÓXIMOS PASOS:")
        print("=" * 100)
        
        print("\n1️⃣  REVISAR RESULTADOS:")
        print("   • Abre los archivos en la carpeta 'resultados/'")
        print("   • Revisa los gráficos en la carpeta 'graficos/'")
        print("   • Lee todos los reportes .txt generados")
        
        print("\n2️⃣  INTERPRETAR:")
        print("   • Los números están calculados, pero TÚ debes interpretarlos")
        print("   • ¿Qué significan los componentes/factores?")
        print("   • ¿Qué representan los clusters?")
        print("   • ¿Tienen sentido en tu contexto?")
        
        print("\n3️⃣  COMPLETAR REFLEXIÓN:")
        print("   • Abre: resultados/plantilla_reflexion_critica.txt")
        print("   • Responde cada pregunta con TUS palabras")
        print("   • Sé honesto sobre tu experiencia")
        
        print("\n4️⃣  REDACTAR INFORME:")
        print("   • Usa los resultados generados")
        print("   • Incluye gráficos y tablas")
        print("   • Explica cada método y sus resultados")
        print("   • Incluye tu reflexión crítica")
        
        print("\n5️⃣  VERIFICAR:")
        print("   • ¿La tabla de codificación tiene mínimo 10 variables? ✓")
        print("   • ¿Aplicaste los 4 métodos (PCA, AFE, Cluster, Discriminante)? ✓")
        print("   • ¿Respondiste las preguntas de cada método? ✓")
        print("   • ¿Hiciste el análisis comparativo? ✓")
        print("   • ¿Completaste la reflexión crítica? ⚠️  (PENDIENTE)")
        
        print("\n" + "=" * 100)
        print("💡 RECUERDA:")
        print("   • La IA calculó los números, TÚ debes interpretarlos")
        print("   • La IA generó plantillas, TÚ debes completarlas")
        print("   • La IA es una herramienta, TÚ eres el analista")
        print("=" * 100)
        
        print("\n🎓 ¡ÉXITO EN TU PROYECTO!")
        
    except Exception as e:
        print(f"\n❌ ERROR GENERAL: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
