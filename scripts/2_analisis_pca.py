"""
Script 2: Análisis de Componentes Principales (ACP/PCA)
Implementa PCA con scree plot, autovalores y cargas factoriales.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from pathlib import Path

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def cargar_y_preparar_datos():
    """Carga y prepara los datos para el análisis"""
    print("📂 Cargando datos...")
    
    # Cargar datos numéricos
    df = pd.read_excel('../BASE_NOMBRES_Y_VALORES.xlsx')
    
    print(f"✓ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # Seleccionar solo columnas numéricas
    df_numeric = df.select_dtypes(include=[np.number])
    
    print(f"✓ Columnas numéricas: {df_numeric.shape[1]}")
    
    # Imputar valores faltantes con la media
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(
        imputer.fit_transform(df_numeric),
        columns=df_numeric.columns
    )
    
    print(f"✓ Valores faltantes imputados")
    
    return df_imputed

def realizar_pca(df, n_components=None):
    """
    Realiza el Análisis de Componentes Principales
    
    Args:
        df: DataFrame con datos numéricos
        n_components: Número de componentes (None = todos)
    """
    print("\n🔬 Realizando Análisis de Componentes Principales...")
    
    # Estandarizar los datos
    scaler = StandardScaler()
    datos_estandarizados = scaler.fit_transform(df)
    
    # Aplicar PCA
    if n_components is None:
        n_components = min(df.shape[0], df.shape[1])
    
    pca = PCA(n_components=n_components)
    componentes = pca.fit_transform(datos_estandarizados)
    
    print(f"✓ PCA completado con {pca.n_components_} componentes")
    
    return pca, componentes, datos_estandarizados

def calcular_componentes_optimos(pca):
    """Determina el número óptimo de componentes"""
    
    # Varianza acumulada
    varianza_acumulada = np.cumsum(pca.explained_variance_ratio_)
    
    # Componentes que explican al menos 80% de varianza
    n_comp_80 = np.argmax(varianza_acumulada >= 0.80) + 1
    
    # Componentes que explican al menos 90% de varianza
    n_comp_90 = np.argmax(varianza_acumulada >= 0.90) + 1
    
    # Criterio de Kaiser (autovalores > 1)
    n_comp_kaiser = np.sum(pca.explained_variance_ > 1)
    
    return {
        '80_varianza': n_comp_80,
        '90_varianza': n_comp_90,
        'kaiser': n_comp_kaiser,
        'varianza_acumulada': varianza_acumulada
    }

def crear_scree_plot(pca, output_dir='../graficos'):
    """Crea el scree plot (gráfico de sedimentación)"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    plt.figure(figsize=(12, 5))
    
    # Subplot 1: Varianza explicada por componente
    plt.subplot(1, 2, 1)
    componentes = range(1, len(pca.explained_variance_ratio_) + 1)
    plt.plot(componentes, pca.explained_variance_ratio_, 'bo-', linewidth=2, markersize=8)
    plt.xlabel('Número de Componente', fontsize=12)
    plt.ylabel('Proporción de Varianza Explicada', fontsize=12)
    plt.title('Scree Plot - Varianza por Componente', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Subplot 2: Varianza acumulada
    plt.subplot(1, 2, 2)
    varianza_acumulada = np.cumsum(pca.explained_variance_ratio_)
    plt.plot(componentes, varianza_acumulada, 'ro-', linewidth=2, markersize=8)
    plt.axhline(y=0.80, color='g', linestyle='--', label='80% varianza')
    plt.axhline(y=0.90, color='b', linestyle='--', label='90% varianza')
    plt.xlabel('Número de Componente', fontsize=12)
    plt.ylabel('Varianza Acumulada', fontsize=12)
    plt.title('Varianza Acumulada', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    path = Path(output_dir) / 'scree_plot.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"\n📊 Scree plot guardado: {path}")
    plt.close()

def crear_tabla_autovalores(pca, output_dir='../resultados'):
    """Crea tabla con autovalores y varianza explicada"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Crear DataFrame con información de autovalores
    n_componentes = min(15, len(pca.explained_variance_))  # Mostrar máximo 15
    
    df_autovalores = pd.DataFrame({
        'Componente': [f'PC{i+1}' for i in range(n_componentes)],
        'Autovalor': pca.explained_variance_[:n_componentes],
        'Varianza_Explicada_%': pca.explained_variance_ratio_[:n_componentes] * 100,
        'Varianza_Acumulada_%': np.cumsum(pca.explained_variance_ratio_[:n_componentes]) * 100
    })
    
    # Guardar
    path = Path(output_dir) / 'tabla_autovalores.xlsx'
    df_autovalores.to_excel(path, index=False)
    print(f"📊 Tabla de autovalores guardada: {path}")
    
    return df_autovalores

def crear_tabla_cargas(pca, columnas, n_componentes=5, output_dir='../resultados'):
    """Crea tabla con cargas factoriales"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Limitar componentes
    n_comp = min(n_componentes, pca.n_components_)
    
    # Crear DataFrame con cargas
    cargas = pca.components_[:n_comp].T
    
    df_cargas = pd.DataFrame(
        cargas,
        columns=[f'PC{i+1}' for i in range(n_comp)],
        index=columnas
    )
    
    # Añadir columna con la carga máxima (en valor absoluto)
    df_cargas['Carga_Maxima'] = df_cargas.abs().max(axis=1)
    df_cargas['Componente_Principal'] = df_cargas.iloc[:, :n_comp].abs().idxmax(axis=1)
    
    # Ordenar por carga máxima
    df_cargas = df_cargas.sort_values('Carga_Maxima', ascending=False)
    
    # Guardar
    path = Path(output_dir) / 'tabla_cargas_factoriales.xlsx'
    df_cargas.to_excel(path)
    print(f"📊 Tabla de cargas factoriales guardada: {path}")
    
    return df_cargas

def crear_mapa_calor_cargas(df_cargas, output_dir='../graficos'):
    """Crea mapa de calor de las cargas factoriales"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Seleccionar solo columnas de componentes
    cols_pc = [col for col in df_cargas.columns if col.startswith('PC')]
    
    # Tomar las 20 variables con mayor carga
    top_vars = df_cargas.nlargest(20, 'Carga_Maxima')[cols_pc]
    
    plt.figure(figsize=(10, 12))
    sns.heatmap(top_vars, cmap='RdBu_r', center=0, annot=True, fmt='.2f',
                cbar_kws={'label': 'Carga Factorial'})
    plt.title('Mapa de Calor - Cargas Factoriales\n(Top 20 variables)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Componentes Principales', fontsize=12)
    plt.ylabel('Variables', fontsize=12)
    plt.tight_layout()
    
    path = Path(output_dir) / 'mapa_calor_cargas.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Mapa de calor guardado: {path}")
    plt.close()

def generar_reporte_pca(pca, criterios, df_autovalores, df_cargas, output_dir='../resultados'):
    """Genera reporte textual del análisis PCA"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    reporte = []
    reporte.append("=" * 80)
    reporte.append("📊 REPORTE DE ANÁLISIS DE COMPONENTES PRINCIPALES (ACP/PCA)")
    reporte.append("=" * 80)
    reporte.append("")
    
    # Pregunta 1: ¿Cuántos componentes retienes?
    reporte.append("1️⃣ ¿CUÁNTOS COMPONENTES RETIENES?")
    reporte.append("-" * 80)
    reporte.append(f"   • Criterio 80% varianza: {criterios['80_varianza']} componentes")
    reporte.append(f"   • Criterio 90% varianza: {criterios['90_varianza']} componentes")
    reporte.append(f"   • Criterio de Kaiser (λ > 1): {criterios['kaiser']} componentes")
    reporte.append("")
    reporte.append(f"   ✅ RECOMENDACIÓN: Retener {criterios['kaiser']} componentes")
    reporte.append("      (Basado en el criterio de Kaiser)")
    reporte.append("")
    
    # Pregunta 2: ¿Qué % de varianza explican?
    reporte.append("2️⃣ ¿QUÉ % DE VARIANZA EXPLICAN?")
    reporte.append("-" * 80)
    for i in range(min(criterios['kaiser'], 10)):
        var_individual = pca.explained_variance_ratio_[i] * 100
        var_acum = criterios['varianza_acumulada'][i] * 100
        reporte.append(f"   • PC{i+1}: {var_individual:.2f}% (Acumulada: {var_acum:.2f}%)")
    reporte.append("")
    
    # Pregunta 3: ¿Qué ítems cargan más en cada componente?
    reporte.append("3️⃣ ¿QUÉ ÍTEMS CARGAN MÁS EN CADA COMPONENTE?")
    reporte.append("-" * 80)
    
    n_comp_mostrar = min(criterios['kaiser'], 5)
    for i in range(n_comp_mostrar):
        pc_name = f'PC{i+1}'
        reporte.append(f"\n   📌 {pc_name}:")
        
        # Top 5 variables con mayor carga (en valor absoluto)
        top_vars = df_cargas[pc_name].abs().nlargest(5)
        for var_name, carga in top_vars.items():
            carga_real = df_cargas.loc[var_name, pc_name]
            reporte.append(f"      • {var_name}: {carga_real:.3f}")
    
    reporte.append("")
    reporte.append("=" * 80)
    
    # Guardar reporte
    reporte_text = "\n".join(reporte)
    print("\n" + reporte_text)
    
    path = Path(output_dir) / 'reporte_pca.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(reporte_text)
    
    print(f"\n💾 Reporte guardado: {path}")

def main():
    """Función principal"""
    print("=" * 80)
    print("🔬 ANÁLISIS 2A: ANÁLISIS DE COMPONENTES PRINCIPALES (ACP/PCA)")
    print("=" * 80)
    
    # 1. Cargar y preparar datos
    df = cargar_y_preparar_datos()
    
    # 2. Realizar PCA
    pca, componentes, datos_std = realizar_pca(df)
    
    # 3. Calcular componentes óptimos
    criterios = calcular_componentes_optimos(pca)
    
    # 4. Crear visualizaciones
    crear_scree_plot(pca)
    
    # 5. Crear tablas
    df_autovalores = crear_tabla_autovalores(pca)
    df_cargas = crear_tabla_cargas(pca, df.columns, n_componentes=criterios['kaiser'])
    
    # 6. Crear mapa de calor
    crear_mapa_calor_cargas(df_cargas)
    
    # 7. Generar reporte
    generar_reporte_pca(pca, criterios, df_autovalores, df_cargas)
    
    print("\n✅ ¡Análisis de PCA completado!")
    
    return pca, componentes, df_cargas

if __name__ == "__main__":
    pca, componentes, df_cargas = main()
