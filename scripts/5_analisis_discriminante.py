"""
Script 5: Análisis Discriminante
Implementa LDA para evaluar discriminación entre grupos.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from pathlib import Path

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def cargar_y_preparar_datos():
    """Carga y prepara los datos"""
    print("📂 Cargando datos...")
    
    df_valores = pd.read_excel('../BASE_NOMBRES_Y_VALORES.xlsx')
    df_etiquetas = pd.read_excel('../BASE_ETIQUETAS.xlsx')
    
    print(f"✓ Valores: {df_valores.shape}")
    print(f"✓ Etiquetas: {df_etiquetas.shape}")
    
    return df_valores, df_etiquetas

def identificar_variable_categorica(df_valores, df_etiquetas):
    """
    Identifica una variable categórica adecuada para el análisis discriminante
    """
    print("\n🔍 Identificando variables categóricas adecuadas...")
    
    candidatos = []
    
    for col in df_valores.columns:
        if col in df_etiquetas.columns:
            # Contar valores únicos
            n_unicos = df_valores[col].nunique()
            
            # Debe tener entre 2 y 5 categorías (ideal para LDA)
            if 2 <= n_unicos <= 5:
                # Verificar que no tenga muchos valores faltantes
                pct_faltantes = df_valores[col].isnull().sum() / len(df_valores) * 100
                
                if pct_faltantes < 50:  # Menos de 50% faltantes
                    candidatos.append({
                        'variable': col,
                        'n_categorias': n_unicos,
                        'pct_faltantes': pct_faltantes,
                        'valores': df_valores[col].value_counts().to_dict()
                    })
    
    if not candidatos:
        print("⚠️  No se encontraron variables categóricas adecuadas")
        print("   Creando variable artificial basada en cuartiles de la primera variable numérica...")
        
        # Crear variable categórica artificial
        primera_numerica = df_valores.select_dtypes(include=[np.number]).columns[0]
        df_valores['Grupo_Artificial'] = pd.qcut(df_valores[primera_numerica].dropna(), 
                                                   q=3, labels=['Bajo', 'Medio', 'Alto'])
        return 'Grupo_Artificial', df_valores
    
    # Ordenar por número de categorías (preferir 2-3 categorías)
    candidatos.sort(key=lambda x: abs(x['n_categorias'] - 2.5))
    
    print(f"\n✓ Se encontraron {len(candidatos)} variables categóricas adecuadas:")
    for i, cand in enumerate(candidatos[:3]):
        print(f"   {i+1}. {cand['variable']}: {cand['n_categorias']} categorías")
        print(f"      Distribución: {cand['valores']}")
    
    # Seleccionar la mejor
    mejor = candidatos[0]['variable']
    print(f"\n✅ Variable seleccionada: {mejor}")
    
    return mejor, df_valores

def preparar_datos_discriminante(df_valores, variable_objetivo):
    """Prepara datos para análisis discriminante"""
    print(f"\n📊 Preparando datos para análisis discriminante...")
    
    # Separar X (predictores) e y (variable objetivo)
    y = df_valores[variable_objetivo].copy()
    X = df_valores.drop(variable_objetivo, axis=1)
    
    # Seleccionar solo columnas numéricas
    X_numeric = X.select_dtypes(include=[np.number])
    
    # Eliminar filas con valores faltantes en y
    mask = y.notna()
    X_numeric = X_numeric[mask]
    y = y[mask]
    
    # Imputar valores faltantes en X
    imputer = SimpleImputer(strategy='mean')
    X_imputed = pd.DataFrame(
        imputer.fit_transform(X_numeric),
        columns=X_numeric.columns,
        index=X_numeric.index
    )
    
    # Codificar variable objetivo si es categórica
    if y.dtype == 'object' or y.dtype.name == 'category':
        le = LabelEncoder()
        y_encoded = le.fit_transform(y)
        clases = le.classes_
    else:
        y_encoded = y.values
        clases = sorted(y.unique())
    
    print(f"✓ Predictores: {X_imputed.shape[1]} variables")
    print(f"✓ Observaciones: {len(y_encoded)}")
    print(f"✓ Clases: {len(np.unique(y_encoded))} - {clases}")
    
    # Distribución de clases
    unique, counts = np.unique(y_encoded, return_counts=True)
    print(f"\n   Distribución de clases:")
    for clase, count in zip(clases, counts):
        pct = count / len(y_encoded) * 100
        print(f"      • {clase}: {count} ({pct:.1f}%)")
    
    return X_imputed, y_encoded, clases

def realizar_analisis_discriminante(X, y, clases):
    """Realiza el análisis discriminante lineal"""
    print(f"\n🔬 Realizando Análisis Discriminante Lineal (LDA)...")
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"✓ Datos de entrenamiento: {len(X_train)}")
    print(f"✓ Datos de prueba: {len(X_test)}")
    
    # Estandarizar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Crear y entrenar modelo LDA
    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train_scaled, y_train)
    
    # Predecir
    y_pred_train = lda.predict(X_train_scaled)
    y_pred_test = lda.predict(X_test_scaled)
    
    # Calcular exactitud
    acc_train = accuracy_score(y_train, y_pred_train)
    acc_test = accuracy_score(y_test, y_pred_test)
    
    print(f"\n✓ Modelo LDA entrenado")
    print(f"   Exactitud en entrenamiento: {acc_train*100:.2f}%")
    print(f"   Exactitud en prueba: {acc_test*100:.2f}%")
    
    return lda, X_test_scaled, y_test, y_pred_test, clases, acc_test

def crear_matriz_confusion(y_true, y_pred, clases, output_dir='../graficos'):
    """Crea y visualiza la matriz de confusión"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=clases, yticklabels=clases,
                cbar_kws={'label': 'Frecuencia'})
    plt.xlabel('Predicción', fontsize=12)
    plt.ylabel('Valor Real', fontsize=12)
    plt.title('Matriz de Confusión - Análisis Discriminante', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    path = Path(output_dir) / 'matriz_confusion_lda.png'
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"\n📊 Matriz de confusión guardada: {path}")
    plt.close()
    
    return cm

def visualizar_discriminantes(lda, X_test, y_test, clases, output_dir='../graficos'):
    """Visualiza las funciones discriminantes"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Transformar datos al espacio discriminante
    X_lda = lda.transform(X_test)
    
    # Si hay más de 1 dimensión, graficar 2D
    if X_lda.shape[1] >= 2:
        plt.figure(figsize=(10, 7))
        
        for i, clase in enumerate(np.unique(y_test)):
            mask = y_test == clase
            plt.scatter(X_lda[mask, 0], X_lda[mask, 1], 
                       label=clases[i], alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
        
        plt.xlabel('LD1 (Primera Función Discriminante)', fontsize=12)
        plt.ylabel('LD2 (Segunda Función Discriminante)', fontsize=12)
        plt.title('Visualización en Espacio Discriminante', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        path = Path(output_dir) / 'espacio_discriminante.png'
        plt.savefig(path, dpi=300, bbox_inches='tight')
        print(f"📊 Visualización discriminante guardada: {path}")
        plt.close()
    
    # Gráfico 1D si solo hay una función discriminante
    elif X_lda.shape[1] == 1:
        plt.figure(figsize=(10, 6))
        
        for i, clase in enumerate(np.unique(y_test)):
            mask = y_test == clase
            plt.hist(X_lda[mask, 0], alpha=0.6, label=clases[i], bins=20)
        
        plt.xlabel('LD1 (Función Discriminante)', fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.title('Distribución en Espacio Discriminante', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        path = Path(output_dir) / 'espacio_discriminante.png'
        plt.savefig(path, dpi=300, bbox_inches='tight')
        print(f"📊 Visualización discriminante guardada: {path}")
        plt.close()

def analizar_coeficientes(lda, nombres_variables, clases, output_dir='../resultados'):
    """Analiza los coeficientes discriminantes"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Obtener coeficientes
    coeficientes = lda.coef_
    
    # Crear DataFrame
    n_funciones = coeficientes.shape[0]
    
    df_coef = pd.DataFrame(
        coeficientes.T,
        columns=[f'LD{i+1}' for i in range(n_funciones)],
        index=nombres_variables
    )
    
    # Añadir importancia (valor absoluto máximo)
    df_coef['Importancia'] = df_coef.abs().max(axis=1)
    df_coef = df_coef.sort_values('Importancia', ascending=False)
    
    # Guardar
    path = Path(output_dir) / 'coeficientes_discriminantes.xlsx'
    df_coef.to_excel(path)
    print(f"📊 Coeficientes discriminantes guardados: {path}")
    
    return df_coef

def generar_reporte_discriminante(variable_obj, clases, accuracy, cm, df_coef, output_dir='../resultados'):
    """Genera reporte del análisis discriminante"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    reporte = []
    reporte.append("=" * 80)
    reporte.append("📊 REPORTE DE ANÁLISIS DISCRIMINANTE LINEAL (LDA)")
    reporte.append("=" * 80)
    reporte.append("")
    
    # Variable objetivo
    reporte.append("1️⃣ VARIABLE CATEGÓRICA SELECCIONADA")
    reporte.append("-" * 80)
    reporte.append(f"   Variable: {variable_obj}")
    reporte.append(f"   Clases: {', '.join(map(str, clases))}")
    reporte.append(f"   Número de clases: {len(clases)}")
    reporte.append("")
    
    # Exactitud
    reporte.append("2️⃣ EXACTITUD DEL MODELO")
    reporte.append("-" * 80)
    reporte.append(f"   Exactitud en datos de prueba: {accuracy*100:.2f}%")
    reporte.append("")
    
    if accuracy > 0.80:
        reporte.append("   ✅ Excelente capacidad discriminante")
    elif accuracy > 0.70:
        reporte.append("   ✅ Buena capacidad discriminante")
    elif accuracy > 0.60:
        reporte.append("   ⚠️  Capacidad discriminante moderada")
    else:
        reporte.append("   ⚠️  Baja capacidad discriminante")
    reporte.append("")
    
    # Matriz de confusión
    reporte.append("3️⃣ MATRIZ DE CONFUSIÓN")
    reporte.append("-" * 80)
    reporte.append("   Ver gráfico: matriz_confusion_lda.png")
    reporte.append("")
    
    # Análisis por clase
    reporte.append("   Métricas por clase:")
    for i, clase in enumerate(clases):
        # Calcular precisión y recall para cada clase
        tp = cm[i, i]
        total_real = cm[i, :].sum()
        total_pred = cm[:, i].sum()
        
        recall = tp / total_real if total_real > 0 else 0
        precision = tp / total_pred if total_pred > 0 else 0
        
        reporte.append(f"      • {clase}:")
        reporte.append(f"        - Recall (sensibilidad): {recall*100:.1f}%")
        reporte.append(f"        - Precisión: {precision*100:.1f}%")
    reporte.append("")
    
    # Variables más importantes
    reporte.append("4️⃣ VARIABLES MÁS IMPORTANTES PARA DISCRIMINACIÓN")
    reporte.append("-" * 80)
    top_vars = df_coef.nlargest(10, 'Importancia')
    for var in top_vars.index:
        importancia = df_coef.loc[var, 'Importancia']
        reporte.append(f"   • {var}: {importancia:.4f}")
    reporte.append("")
    
    # Conclusión
    reporte.append("5️⃣ CONCLUSIÓN")
    reporte.append("-" * 80)
    reporte.append("   El análisis discriminante permite:")
    reporte.append(f"   ✓ Clasificar observaciones en {len(clases)} grupos")
    reporte.append(f"   ✓ Con una exactitud de {accuracy*100:.2f}%")
    reporte.append("   ✓ Las variables listadas arriba son las más discriminantes")
    reporte.append("")
    
    if len(clases) == 2:
        reporte.append("   📌 Con 2 clases, LDA crea 1 función discriminante")
    else:
        reporte.append(f"   📌 Con {len(clases)} clases, LDA crea {len(clases)-1} funciones discriminantes")
    
    reporte.append("")
    reporte.append("=" * 80)
    
    # Guardar e imprimir
    reporte_text = "\n".join(reporte)
    print("\n" + reporte_text)
    
    path = Path(output_dir) / 'reporte_discriminante.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(reporte_text)
    
    print(f"\n💾 Reporte guardado: {path}")

def main():
    """Función principal"""
    print("=" * 80)
    print("🔬 ANÁLISIS 2D: ANÁLISIS DISCRIMINANTE LINEAL (LDA)")
    print("=" * 80)
    
    # 1. Cargar datos
    df_valores, df_etiquetas = cargar_y_preparar_datos()
    
    # 2. Identificar variable categórica
    variable_obj, df_valores = identificar_variable_categorica(df_valores, df_etiquetas)
    
    # 3. Preparar datos
    X, y, clases = preparar_datos_discriminante(df_valores, variable_obj)
    
    # 4. Realizar análisis discriminante
    lda, X_test, y_test, y_pred, clases, accuracy = realizar_analisis_discriminante(X, y, clases)
    
    # 5. Crear matriz de confusión
    cm = crear_matriz_confusion(y_test, y_pred, clases)
    
    # 6. Visualizar funciones discriminantes
    visualizar_discriminantes(lda, X_test, y_test, clases)
    
    # 7. Analizar coeficientes
    df_coef = analizar_coeficientes(lda, X.columns, clases)
    
    # 8. Generar reporte
    generar_reporte_discriminante(variable_obj, clases, accuracy, cm, df_coef)
    
    print("\n✅ ¡Análisis Discriminante completado!")
    
    return lda, accuracy, cm

if __name__ == "__main__":
    lda, accuracy, cm = main()
