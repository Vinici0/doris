"""
Script 1: Hoja de Codificación
Compara BASE_ETIQUETAS.xlsx con BASE_NOMBRES_Y_VALORES.xlsx
para determinar la codificación de cada variable.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def cargar_datos():
    """Carga los dos archivos Excel"""
    print("📂 Cargando archivos Excel...")
    
    etiquetas = pd.read_excel('../BASE_ETIQUETAS.xlsx')
    valores = pd.read_excel('../BASE_NOMBRES_Y_VALORES.xlsx')
    
    print(f"✓ BASE_ETIQUETAS: {etiquetas.shape[0]} filas, {etiquetas.shape[1]} columnas")
    print(f"✓ BASE_NOMBRES_Y_VALORES: {valores.shape[0]} filas, {valores.shape[1]} columnas")
    
    return etiquetas, valores

def analizar_codificacion(etiquetas, valores, max_variables=15):
    """
    Analiza y crea la tabla de codificación comparando ambos archivos
    
    Args:
        etiquetas: DataFrame con las etiquetas
        valores: DataFrame con los valores codificados
        max_variables: Número máximo de variables a analizar
    """
    print("\n📊 Analizando codificación de variables...")
    
    # Lista para almacenar la información de codificación
    codificacion_data = []
    
    # Obtener las columnas comunes
    columnas_comunes = list(set(etiquetas.columns) & set(valores.columns))
    
    # Limitar al número deseado de variables
    columnas_analizar = columnas_comunes[:min(max_variables, len(columnas_comunes))]
    
    for col in columnas_analizar:
        # Obtener valores únicos de la columna en valores
        valores_unicos = valores[col].dropna().unique()
        
        # Obtener etiquetas únicas de la columna en etiquetas
        etiquetas_unicas = etiquetas[col].dropna().unique()
        
        # Crear el mapeo de codificación
        codificacion = {}
        
        # Si hay valores numéricos y etiquetas de texto, crear el mapeo
        if len(valores_unicos) > 0 and len(etiquetas_unicas) > 0:
            # Ordenar valores únicos para mapeo consistente
            valores_ordenados = sorted([v for v in valores_unicos if pd.notna(v)])
            etiquetas_ordenadas = sorted([e for e in etiquetas_unicas if pd.notna(e)])
            
            # Crear mapeo
            for i, (val, etiq) in enumerate(zip(valores_ordenados, etiquetas_ordenadas)):
                codificacion[val] = etiq
        
        # Si no hay mapeo claro, usar los valores directamente
        if not codificacion and len(valores_unicos) > 0:
            for val in sorted(valores_unicos)[:5]:  # Máximo 5 valores
                codificacion[val] = f"Valor {val}"
        
        # Crear la descripción de codificación
        if codificacion:
            cod_str = " / ".join([f"{k} = {v}" for k, v in list(codificacion.items())[:6]])
        else:
            cod_str = "Variable continua o sin codificación clara"
        
        # Intentar determinar una descripción de la variable
        descripcion = determinar_descripcion(col, etiquetas_unicas)
        
        codificacion_data.append({
            'Variable': col,
            'Descripción': descripcion,
            'Codificación': cod_str,
            'N_Valores': len(valores_unicos)
        })
    
    # Crear DataFrame con la codificación
    df_codificacion = pd.DataFrame(codificacion_data)
    
    print(f"\n✓ Se analizaron {len(df_codificacion)} variables")
    
    return df_codificacion

def determinar_descripcion(nombre_variable, etiquetas):
    """Determina una descripción basada en el nombre de la variable y sus etiquetas"""
    
    # Diccionario de palabras clave comunes
    palabras_clave = {
        'sexo': 'Sexo',
        'edad': 'Edad',
        'embarazo': 'Estado de embarazo',
        'peso': 'Peso',
        'talla': 'Talla/Altura',
        'imc': 'Índice de Masa Corporal',
        'presion': 'Presión arterial',
        'diabetes': 'Diabetes',
        'estado': 'Estado',
        'civil': 'Estado civil',
        'educacion': 'Nivel educativo',
        'ingreso': 'Nivel de ingresos',
        'trabajo': 'Situación laboral'
    }
    
    nombre_lower = str(nombre_variable).lower()
    
    # Buscar coincidencias en el nombre
    for palabra, descripcion in palabras_clave.items():
        if palabra in nombre_lower:
            return descripcion
    
    # Si hay etiquetas, usar la primera como pista
    if len(etiquetas) > 0:
        primera_etiqueta = str(etiquetas[0])
        if len(primera_etiqueta) < 50:
            return f"Variable relacionada con {primera_etiqueta}"
    
    return f"Variable {nombre_variable}"

def guardar_resultados(df_codificacion, output_dir='../resultados'):
    """Guarda la tabla de codificación en Excel y CSV"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Guardar en Excel
    excel_path = Path(output_dir) / 'tabla_codificacion.xlsx'
    df_codificacion.to_excel(excel_path, index=False)
    print(f"\n💾 Tabla guardada en Excel: {excel_path}")
    
    # Guardar en CSV
    csv_path = Path(output_dir) / 'tabla_codificacion.csv'
    df_codificacion.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"💾 Tabla guardada en CSV: {csv_path}")
    
    return excel_path

def mostrar_tabla(df_codificacion):
    """Muestra la tabla de codificación en consola"""
    print("\n" + "="*100)
    print("📋 TABLA DE CODIFICACIÓN DE VARIABLES")
    print("="*100)
    print(df_codificacion.to_string(index=False))
    print("="*100)

def main():
    """Función principal"""
    print("="*80)
    print("🔢 ANÁLISIS 1: HOJA DE CODIFICACIÓN")
    print("="*80)
    
    # Cargar datos
    etiquetas, valores = cargar_datos()
    
    # Analizar codificación (mínimo 10 variables)
    df_codificacion = analizar_codificacion(etiquetas, valores, max_variables=15)
    
    # Mostrar tabla
    mostrar_tabla(df_codificacion)
    
    # Guardar resultados
    guardar_resultados(df_codificacion)
    
    print("\n✅ ¡Análisis completado!")
    print("\n📌 Esta tabla debe incluirse en tu informe final.")
    
    return df_codificacion

if __name__ == "__main__":
    df_cod = main()
