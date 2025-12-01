"""
Script 3: Análisis Factorial Exploratorio (AFE)
Implementa AFE, evalúa cargas factoriales y compara con PCA.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity, calculate_kmo
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from pathlib import Path

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def cargar_y_preparar_datos():
    """Carga y prepara los datos para el análisis"""
    print("📂 Cargando datos...")
    
    df = pd.read_excel('../BASE_NOMBRES_Y_VALORES.xlsx')
    print(f"✓ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # Seleccionar solo columnas numéricas
    df_numeric = df.select_dtypes(include=[np.number])
    print(f"✓ Columnas numéricas: {df_numeric.shape[1]}")
    
    # Imputar valores faltantes
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(
        imputer.fit_transform(df_numeric),
        columns=df_numeric.columns
    )
    
    print(f"✓ Valores faltantes imputados")
    
    return df_imputed

def evaluar_adecuacion_muestral(df):
    """
    Evalúa si los datos son adecuados para análisis factorial
    usando KMO y test de Bartlett
    """
    print("\n🔍 Evaluando adecuación muestral...")
    
    # Test de esfericidad de Bartlett
    chi_square_value, p_value = calculate_bartlett_sphericity(df)
    
    print(f"\n📊 Test de Bartlett:")
    print(f"   Chi-cuadrado: {chi_square_value:.2f}")
    print(f"   p-valor: {p_value:.6f}")
    
    if p_value < 0.05:
        print(f"   ✅ Los datos son adecuados para factorial (p < 0.05)")
    else:
        print(f"   ⚠️  Los datos podrían no ser ideales (p >= 0.05)")
    
    # KMO (Kaiser-Meyer-Olkin)
    kmo_all, kmo_model = calculate_kmo(df)
    
    print(f"\n📊 Medida KMO:")
    print(f"   KMO global: {kmo_model:.3f}")
    
    if kmo_model >= 0.9:
        print(f"   ✅ Excelente")
    elif kmo_model >= 0.8:
        print(f"   ✅ Muy bueno")
    elif kmo_model >= 0.7:
        print(f"   ✅ Aceptable")
    elif kmo_model >= 0.6:
        print(f"   ⚠️  Mediocre")
    else:
        print(f"   ❌ Inadecuado")
    
    return {'bartlett_p': p_value, 'kmo': kmo_model}

def determinar_numero_factores(df, max_factors=10):
    """Determina el número óptimo de factores"""
    print("\n🔢 Determinando número óptimo de factores...")
    
    # Probar diferentes números de factores
    max_factors = min(max_factors, df.shape[1] - 1)
    
    # Análisis inicial para obtener autovalores
    fa_initial = FactorAnalyzer(n_factors=max_factors, rotation=None)
    fa_initial.fit(df)
    
    # Obtener autovalores
    ev, _ = fa_initial.get_eigenvalues()
    
    # Criterio de Kaiser (autovalores > 1)
    n_factores_kaiser = np.sum(ev > 1)
    
    print(f"\n✓ Autovalores calculados")
    print(f"✓ Factores con autovalor > 1: {n_factores_kaiser}")
    
    # Crear gráfico de sedimentación
    crear_scree_plot_afe(ev)
    
    return n_factores_kaiser, ev

def crear_scree_plot_afe(eigenvalues, output_dir='../graficos'):
    """Crea scree plot para AFE"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    factores = range(1, len(eigenvalues) + 1)
    plt.plot(factores, eigenvalues, 'bo-', linewidth=2, markersize=8)
    plt.axhline(y=1, color='r', linestyle='--', label='Criterio Kaiser (λ=1)')
    plt.xlabel('Número de Factor', fontsize=12)
    plt.ylabel('Autovalor', fontsize=12)
    plt.title('Scree Plot - Análisis Factorial Exploratorio', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    path = Path(output_dir) / 'scree_plot_afe.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Scree plot AFE guardado: {path}")
    plt.close()

def realizar_afe(df, n_factors, rotation='varimax'):
    """
    Realiza el Análisis Factorial Exploratorio
    
    Args:
        df: DataFrame con datos
        n_factors: Número de factores
        rotation: Método de rotación ('varimax', 'promax', None)
    """
    print(f"\n🔬 Realizando AFE con {n_factors} factores (rotación: {rotation})...")
    
    # Crear y ajustar modelo
    fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation)
    fa.fit(df)
    
    print(f"✓ AFE completado")
    
    # Obtener cargas factoriales
    loadings = fa.loadings_
    
    # Crear DataFrame con cargas
    df_loadings = pd.DataFrame(
        loadings,
        columns=[f'Factor{i+1}' for i in range(n_factors)],
        index=df.columns
    )
    
    # Calcular comunalidades
    communalities = fa.get_communalities()
    df_loadings['Comunalidad'] = communalities
    
    # Calcular varianza explicada
    variance = fa.get_factor_variance()
    
    return fa, df_loadings, variance

def crear_tabla_cargas_afe(df_loadings, output_dir='../resultados'):
    """Crea tabla con cargas factoriales del AFE"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Añadir columna con factor dominante
    factor_cols = [col for col in df_loadings.columns if col.startswith('Factor')]
    df_loadings['Factor_Dominante'] = df_loadings[factor_cols].abs().idxmax(axis=1)
    df_loadings['Carga_Maxima'] = df_loadings[factor_cols].abs().max(axis=1)
    
    # Ordenar por factor dominante y carga
    df_sorted = df_loadings.sort_values(['Factor_Dominante', 'Carga_Maxima'], 
                                         ascending=[True, False])
    
    # Guardar
    path = Path(output_dir) / 'tabla_cargas_afe.xlsx'
    df_sorted.to_excel(path)
    print(f"📊 Tabla de cargas AFE guardada: {path}")
    
    return df_sorted

def crear_mapa_calor_afe(df_loadings, output_dir='../graficos'):
    """Crea mapa de calor de cargas AFE"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Seleccionar solo columnas de factores
    factor_cols = [col for col in df_loadings.columns if col.startswith('Factor')]
    
    # Tomar top 20 variables por carga máxima
    top_vars = df_loadings.nlargest(20, 'Carga_Maxima')[factor_cols]
    
    plt.figure(figsize=(10, 12))
    sns.heatmap(top_vars, cmap='RdBu_r', center=0, annot=True, fmt='.2f',
                cbar_kws={'label': 'Carga Factorial'})
    plt.title('Mapa de Calor - Cargas Factoriales AFE\n(Top 20 variables)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Factores', fontsize=12)
    plt.ylabel('Variables', fontsize=12)
    plt.tight_layout()
    
    path = Path(output_dir) / 'mapa_calor_afe.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"📊 Mapa de calor AFE guardado: {path}")
    plt.close()

def comparar_con_pca(df_loadings, output_dir='../resultados'):
    """Compara resultados de AFE con PCA"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    comparacion = []
    comparacion.append("=" * 80)
    comparacion.append("🔄 COMPARACIÓN AFE vs PCA")
    comparacion.append("=" * 80)
    comparacion.append("")
    
    comparacion.append("📌 SIMILITUDES:")
    comparacion.append("   • Ambos son métodos de reducción de dimensionalidad")
    comparacion.append("   • Ambos identifican patrones subyacentes en los datos")
    comparacion.append("   • Ambos usan rotación para mejorar interpretabilidad")
    comparacion.append("")
    
    comparacion.append("📌 DIFERENCIAS CLAVE:")
    comparacion.append("   • PCA: Maximiza varianza explicada (componentes ortogonales)")
    comparacion.append("   • AFE: Busca factores latentes que causan las correlaciones")
    comparacion.append("   • PCA: Más matemático/estadístico")
    comparacion.append("   • AFE: Más teórico/conceptual")
    comparacion.append("")
    
    comparacion.append("📌 INTERPRETACIÓN:")
    comparacion.append("   • Las cargas factoriales muestran qué variables se agrupan")
    comparacion.append("   • Factores con cargas altas (>0.4) son más relevantes")
    comparacion.append("   • Variables con comunalidades bajas (<0.3) son poco explicadas")
    comparacion.append("")
    
    # Análisis de comunalidades
    comunalidades_bajas = df_loadings[df_loadings['Comunalidad'] < 0.3]
    if len(comunalidades_bajas) > 0:
        comparacion.append(f"⚠️  VARIABLES CON BAJA COMUNALIDAD (<0.3): {len(comunalidades_bajas)}")
        for var in comunalidades_bajas.head(5).index:
            com = df_loadings.loc[var, 'Comunalidad']
            comparacion.append(f"   • {var}: {com:.3f}")
    else:
        comparacion.append("✅ Todas las variables tienen comunalidades aceptables (>0.3)")
    
    comparacion.append("")
    comparacion.append("=" * 80)
    
    comparacion_text = "\n".join(comparacion)
    print("\n" + comparacion_text)
    
    # Guardar
    path = Path(output_dir) / 'comparacion_afe_pca.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(comparacion_text)
    
    print(f"\n💾 Comparación guardada: {path}")

def generar_reporte_afe(n_factors, df_loadings, variance, adecuacion, output_dir='../resultados'):
    """Genera reporte completo del AFE"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    reporte = []
    reporte.append("=" * 80)
    reporte.append("📊 REPORTE DE ANÁLISIS FACTORIAL EXPLORATORIO (AFE)")
    reporte.append("=" * 80)
    reporte.append("")
    
    # Adecuación muestral
    reporte.append("1️⃣ ADECUACIÓN DE LOS DATOS")
    reporte.append("-" * 80)
    reporte.append(f"   • KMO: {adecuacion['kmo']:.3f}")
    reporte.append(f"   • Test de Bartlett (p-valor): {adecuacion['bartlett_p']:.6f}")
    reporte.append("")
    
    # Número de factores
    reporte.append("2️⃣ NÚMERO DE FACTORES ELEGIDOS")
    reporte.append("-" * 80)
    reporte.append(f"   ✅ Se retuvieron {n_factors} factores")
    reporte.append("      (Basado en criterio de Kaiser: autovalores > 1)")
    reporte.append("")
    
    # Varianza explicada
    reporte.append("3️⃣ VARIANZA EXPLICADA POR FACTOR")
    reporte.append("-" * 80)
    for i in range(n_factors):
        var_prop = variance[0][i] * 100  # Proporción de varianza
        var_acum = variance[2][i] * 100   # Varianza acumulada
        reporte.append(f"   • Factor{i+1}: {var_prop:.2f}% (Acumulada: {var_acum:.2f}%)")
    reporte.append("")
    
    # Variables por factor
    reporte.append("4️⃣ VARIABLES MÁS RELEVANTES POR FACTOR")
    reporte.append("-" * 80)
    
    factor_cols = [col for col in df_loadings.columns if col.startswith('Factor')]
    for factor in factor_cols:
        reporte.append(f"\n   📌 {factor}:")
        top_vars = df_loadings[factor].abs().nlargest(5)
        for var_name, carga in top_vars.items():
            carga_real = df_loadings.loc[var_name, factor]
            comunalidad = df_loadings.loc[var_name, 'Comunalidad']
            reporte.append(f"      • {var_name}: {carga_real:.3f} (h²={comunalidad:.3f})")
    
    reporte.append("")
    
    # Coherencia de factores
    reporte.append("5️⃣ COHERENCIA DE FACTORES")
    reporte.append("-" * 80)
    reporte.append("   Los factores son coherentes si:")
    reporte.append("   ✓ Las variables con altas cargas tienen sentido temático")
    reporte.append("   ✓ Las comunalidades son generalmente > 0.3")
    reporte.append("   ✓ Cada factor representa un constructo interpretable")
    reporte.append("")
    reporte.append("   👉 REVISAR EL MAPA DE CALOR Y LAS TABLAS PARA EVALUAR COHERENCIA")
    reporte.append("")
    
    reporte.append("=" * 80)
    
    # Guardar e imprimir
    reporte_text = "\n".join(reporte)
    print("\n" + reporte_text)
    
    path = Path(output_dir) / 'reporte_afe.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(reporte_text)
    
    print(f"\n💾 Reporte guardado: {path}")

def main():
    """Función principal"""
    print("=" * 80)
    print("🔬 ANÁLISIS 2B: ANÁLISIS FACTORIAL EXPLORATORIO (AFE)")
    print("=" * 80)
    
    # 1. Cargar datos
    df = cargar_y_preparar_datos()
    
    # 2. Evaluar adecuación muestral
    adecuacion = evaluar_adecuacion_muestral(df)
    
    # 3. Determinar número de factores
    n_factors, eigenvalues = determinar_numero_factores(df)
    
    # 4. Realizar AFE
    fa, df_loadings, variance = realizar_afe(df, n_factors)
    
    # 5. Crear tablas y gráficos
    df_loadings_sorted = crear_tabla_cargas_afe(df_loadings)
    crear_mapa_calor_afe(df_loadings)
    
    # 6. Comparar con PCA
    comparar_con_pca(df_loadings)
    
    # 7. Generar reporte
    generar_reporte_afe(n_factors, df_loadings, variance, adecuacion)
    
    print("\n✅ ¡Análisis Factorial Exploratorio completado!")
    
    return fa, df_loadings

if __name__ == "__main__":
    fa, df_loadings = main()
