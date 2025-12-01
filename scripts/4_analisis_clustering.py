"""
Script 4: Análisis de Cluster (Agrupamiento)
Implementa K-means con método del codo y descripción de grupos.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from pathlib import Path

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def cargar_y_preparar_datos():
    """Carga y prepara los datos para clustering"""
    print("📂 Cargando datos...")
    
    df = pd.read_excel('../BASE_NOMBRES_Y_VALORES.xlsx')
    print(f"✓ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # Seleccionar columnas numéricas
    df_numeric = df.select_dtypes(include=[np.number])
    print(f"✓ Columnas numéricas: {df_numeric.shape[1]}")
    
    # Imputar valores faltantes
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(
        imputer.fit_transform(df_numeric),
        columns=df_numeric.columns
    )
    
    # Estandarizar datos
    scaler = StandardScaler()
    datos_estandarizados = scaler.fit_transform(df_imputed)
    
    df_scaled = pd.DataFrame(
        datos_estandarizados,
        columns=df_numeric.columns
    )
    
    print(f"✓ Datos estandarizados")
    
    return df_scaled, df_imputed

def metodo_del_codo(df, max_clusters=10, output_dir='../graficos'):
    """
    Implementa el método del codo para determinar número óptimo de clusters
    """
    print(f"\n📊 Aplicando método del codo (probando 2-{max_clusters} clusters)...")
    
    # Listas para almacenar métricas
    inercias = []
    silhouette_scores = []
    calinski_scores = []
    davies_bouldin_scores = []
    
    range_clusters = range(2, max_clusters + 1)
    
    for k in range_clusters:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(df)
        
        # Calcular métricas
        inercias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(df, labels))
        calinski_scores.append(calinski_harabasz_score(df, labels))
        davies_bouldin_scores.append(davies_bouldin_score(df, labels))
        
        print(f"   K={k}: Inercia={kmeans.inertia_:.2f}, Silhouette={silhouette_scores[-1]:.3f}")
    
    # Crear gráfico del codo
    crear_graficos_metricas(range_clusters, inercias, silhouette_scores, 
                           calinski_scores, davies_bouldin_scores, output_dir)
    
    # Determinar mejor K usando silhouette
    mejor_k = range_clusters[np.argmax(silhouette_scores)]
    
    print(f"\n✅ Mejor número de clusters (según Silhouette): {mejor_k}")
    
    return mejor_k, {
        'inercias': inercias,
        'silhouette': silhouette_scores,
        'calinski': calinski_scores,
        'davies_bouldin': davies_bouldin_scores
    }

def crear_graficos_metricas(range_clusters, inercias, silhouette, calinski, davies, output_dir):
    """Crea gráficos de las métricas de clustering"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Gráfico 1: Método del codo (Inercia)
    axes[0, 0].plot(range_clusters, inercias, 'bo-', linewidth=2, markersize=8)
    axes[0, 0].set_xlabel('Número de Clusters', fontsize=11)
    axes[0, 0].set_ylabel('Inercia (WCSS)', fontsize=11)
    axes[0, 0].set_title('Método del Codo', fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Gráfico 2: Coeficiente de Silhouette
    axes[0, 1].plot(range_clusters, silhouette, 'go-', linewidth=2, markersize=8)
    axes[0, 1].set_xlabel('Número de Clusters', fontsize=11)
    axes[0, 1].set_ylabel('Coeficiente de Silhouette', fontsize=11)
    axes[0, 1].set_title('Coeficiente de Silhouette (mayor es mejor)', fontsize=12, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0.5, color='r', linestyle='--', alpha=0.5, label='Umbral 0.5')
    axes[0, 1].legend()
    
    # Gráfico 3: Índice Calinski-Harabasz
    axes[1, 0].plot(range_clusters, calinski, 'ro-', linewidth=2, markersize=8)
    axes[1, 0].set_xlabel('Número de Clusters', fontsize=11)
    axes[1, 0].set_ylabel('Índice Calinski-Harabasz', fontsize=11)
    axes[1, 0].set_title('Calinski-Harabasz (mayor es mejor)', fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Gráfico 4: Índice Davies-Bouldin
    axes[1, 1].plot(range_clusters, davies, 'mo-', linewidth=2, markersize=8)
    axes[1, 1].set_xlabel('Número de Clusters', fontsize=11)
    axes[1, 1].set_ylabel('Índice Davies-Bouldin', fontsize=11)
    axes[1, 1].set_title('Davies-Bouldin (menor es mejor)', fontsize=12, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    path = Path(output_dir) / 'metricas_clustering.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Gráficos de métricas guardados: {path}")
    plt.close()

def realizar_clustering(df, n_clusters):
    """Realiza clustering con K-means"""
    print(f"\n🔬 Realizando clustering con {n_clusters} grupos...")
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df)
    
    print(f"✓ Clustering completado")
    
    return kmeans, labels

def describir_clusters(df_original, labels, n_clusters, output_dir='../resultados'):
    """Describe cada cluster basándose en las características promedio"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    print(f"\n📝 Describiendo clusters...")
    
    # Añadir etiquetas al DataFrame
    df_con_clusters = df_original.copy()
    df_con_clusters['Cluster'] = labels
    
    # Calcular estadísticas por cluster
    descripciones = []
    
    for cluster_id in range(n_clusters):
        cluster_data = df_con_clusters[df_con_clusters['Cluster'] == cluster_id]
        n_miembros = len(cluster_data)
        
        # Calcular medias
        medias = cluster_data.drop('Cluster', axis=1).mean()
        
        # Encontrar características más distintivas (mayor desviación de la media global)
        media_global = df_original.mean()
        diferencias = abs(medias - media_global)
        top_caracteristicas = diferencias.nlargest(5)
        
        descripciones.append({
            'Cluster': f'Cluster {cluster_id}',
            'N_Miembros': n_miembros,
            'Porcentaje': f'{(n_miembros/len(df_con_clusters)*100):.1f}%',
            'Top_Caracteristicas': top_caracteristicas.to_dict()
        })
    
    # Crear DataFrame de descripción
    df_descripcion = pd.DataFrame(descripciones)
    
    # Guardar estadísticas detalladas
    stats_completas = df_con_clusters.groupby('Cluster').mean()
    
    path_stats = Path(output_dir) / 'estadisticas_clusters.xlsx'
    stats_completas.to_excel(path_stats)
    print(f"📊 Estadísticas de clusters guardadas: {path_stats}")
    
    path_desc = Path(output_dir) / 'descripcion_clusters.xlsx'
    df_descripcion.to_excel(path_desc, index=False)
    print(f"📊 Descripción de clusters guardada: {path_desc}")
    
    return df_con_clusters, df_descripcion, stats_completas

def visualizar_clusters_2d(df_scaled, labels, n_clusters, output_dir='../graficos'):
    """Visualiza clusters en 2D usando las dos primeras componentes principales"""
    
    from sklearn.decomposition import PCA
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Reducir a 2D con PCA
    pca = PCA(n_components=2)
    datos_2d = pca.fit_transform(df_scaled)
    
    # Crear gráfico
    plt.figure(figsize=(12, 8))
    
    scatter = plt.scatter(datos_2d[:, 0], datos_2d[:, 1], 
                         c=labels, cmap='viridis', 
                         s=50, alpha=0.6, edgecolors='black', linewidth=0.5)
    
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varianza)', fontsize=12)
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varianza)', fontsize=12)
    plt.title(f'Visualización de Clusters (K={n_clusters})', fontsize=14, fontweight='bold')
    plt.colorbar(scatter, label='Cluster')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    path = Path(output_dir) / 'visualizacion_clusters.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Visualización de clusters guardada: {path}")
    plt.close()

def interpretar_clusters(df_descripcion, stats_completas, output_dir='../resultados'):
    """Genera interpretación narrativa de los clusters"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    interpretacion = []
    interpretacion.append("=" * 80)
    interpretacion.append("🎯 INTERPRETACIÓN DE CLUSTERS")
    interpretacion.append("=" * 80)
    interpretacion.append("")
    
    for idx, row in df_descripcion.iterrows():
        cluster_name = row['Cluster']
        n_miembros = row['N_Miembros']
        porcentaje = row['Porcentaje']
        
        interpretacion.append(f"\n📌 {cluster_name}")
        interpretacion.append("-" * 80)
        interpretacion.append(f"   Tamaño: {n_miembros} personas ({porcentaje})")
        interpretacion.append("")
        interpretacion.append("   Características distintivas:")
        
        # Mostrar top características
        top_cars = row['Top_Caracteristicas']
        for var, valor in list(top_cars.items())[:5]:
            interpretacion.append(f"      • {var}: {valor:.3f}")
        
        interpretacion.append("")
        interpretacion.append("   💡 Perfil del grupo:")
        interpretacion.append(f"      Este grupo representa un {porcentaje} de la muestra.")
        interpretacion.append("      Se caracteriza por los valores mostrados arriba.")
        interpretacion.append("      [INTERPRETAR MANUALMENTE según el contexto de tus datos]")
    
    interpretacion.append("")
    interpretacion.append("=" * 80)
    interpretacion.append("👥 TIPOS DE PERSONAS EN CADA GRUPO")
    interpretacion.append("=" * 80)
    interpretacion.append("")
    interpretacion.append("⚠️  NOTA IMPORTANTE:")
    interpretacion.append("La interpretación final debe hacerse manualmente considerando:")
    interpretacion.append("   • El contexto de tu estudio")
    interpretacion.append("   • El significado de cada variable")
    interpretacion.append("   • Los patrones observados en las estadísticas")
    interpretacion.append("")
    interpretacion.append("Ejemplo de interpretación:")
    interpretacion.append("   • Cluster 0: Personas jóvenes con alto nivel educativo")
    interpretacion.append("   • Cluster 1: Adultos mayores con condiciones de salud específicas")
    interpretacion.append("   • Cluster 2: Grupo intermedio con características balanceadas")
    interpretacion.append("")
    interpretacion.append("=" * 80)
    
    # Guardar e imprimir
    interpretacion_text = "\n".join(interpretacion)
    print("\n" + interpretacion_text)
    
    path = Path(output_dir) / 'interpretacion_clusters.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(interpretacion_text)
    
    print(f"\n💾 Interpretación guardada: {path}")

def generar_reporte_clustering(n_clusters, metricas, df_descripcion, output_dir='../resultados'):
    """Genera reporte completo del análisis de clustering"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    reporte = []
    reporte.append("=" * 80)
    reporte.append("📊 REPORTE DE ANÁLISIS DE CLUSTERING")
    reporte.append("=" * 80)
    reporte.append("")
    
    # Metodología
    reporte.append("1️⃣ METODOLOGÍA")
    reporte.append("-" * 80)
    reporte.append("   • Algoritmo: K-Means")
    reporte.append("   • Datos: Estandarizados (media=0, sd=1)")
    reporte.append("   • Métrica: Distancia Euclidiana")
    reporte.append("")
    
    # Número óptimo de clusters
    reporte.append("2️⃣ DETERMINACIÓN DEL NÚMERO ÓPTIMO DE CLUSTERS")
    reporte.append("-" * 80)
    reporte.append(f"   ✅ Clusters elegidos: {n_clusters}")
    reporte.append("")
    reporte.append("   Método del codo:")
    reporte.append("      • Evaluamos de 2 a 10 clusters")
    reporte.append("      • Usamos 4 métricas de validación:")
    reporte.append("        - Inercia (WCSS)")
    reporte.append("        - Coeficiente de Silhouette")
    reporte.append("        - Índice Calinski-Harabasz")
    reporte.append("        - Índice Davies-Bouldin")
    reporte.append("")
    
    # Calidad del clustering
    reporte.append("3️⃣ CALIDAD DEL CLUSTERING")
    reporte.append("-" * 80)
    idx = n_clusters - 2  # Ajustar índice
    reporte.append(f"   • Silhouette Score: {metricas['silhouette'][idx]:.3f}")
    if metricas['silhouette'][idx] > 0.5:
        reporte.append("     ✅ Buena separación entre clusters")
    elif metricas['silhouette'][idx] > 0.3:
        reporte.append("     ⚠️  Separación aceptable")
    else:
        reporte.append("     ⚠️  Separación débil, considerar otros valores de K")
    reporte.append("")
    
    # Descripción de grupos
    reporte.append("4️⃣ DESCRIPCIÓN DE GRUPOS")
    reporte.append("-" * 80)
    for idx, row in df_descripcion.iterrows():
        reporte.append(f"   • {row['Cluster']}: {row['N_Miembros']} miembros ({row['Porcentaje']})")
    reporte.append("")
    reporte.append("   Ver 'interpretacion_clusters.txt' para detalles completos")
    reporte.append("")
    
    reporte.append("=" * 80)
    
    # Guardar e imprimir
    reporte_text = "\n".join(reporte)
    print("\n" + reporte_text)
    
    path = Path(output_dir) / 'reporte_clustering.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(reporte_text)
    
    print(f"\n💾 Reporte guardado: {path}")

def main():
    """Función principal"""
    print("=" * 80)
    print("🔬 ANÁLISIS 2C: ANÁLISIS DE CLUSTERING (K-MEANS)")
    print("=" * 80)
    
    # 1. Cargar y preparar datos
    df_scaled, df_original = cargar_y_preparar_datos()
    
    # 2. Método del codo
    mejor_k, metricas = metodo_del_codo(df_scaled, max_clusters=10)
    
    # 3. Realizar clustering
    kmeans, labels = realizar_clustering(df_scaled, mejor_k)
    
    # 4. Describir clusters
    df_con_clusters, df_descripcion, stats = describir_clusters(df_original, labels, mejor_k)
    
    # 5. Visualizar clusters
    visualizar_clusters_2d(df_scaled, labels, mejor_k)
    
    # 6. Interpretar clusters
    interpretar_clusters(df_descripcion, stats)
    
    # 7. Generar reporte
    generar_reporte_clustering(mejor_k, metricas, df_descripcion)
    
    print("\n✅ ¡Análisis de Clustering completado!")
    
    return kmeans, labels, df_con_clusters

if __name__ == "__main__":
    kmeans, labels, df_con_clusters = main()
