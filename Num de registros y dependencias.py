import json

# Ruta del archivo JSON
file_path = "C:\\Users\\adria\\Downloads\\s6-muestra-100contrataciones.json"

# Función para imprimir campos específicos y sus valores
def print_specific_fields(record):
    record_id = record.get('_id', 'N/A')
    buyer_name = record.get('buyer', {}).get('name', 'N/A')
    
    awards = record.get('awards', [])
    awards_description = awards[0].get('description', 'N/A') if awards else 'N/A'
    awards_supplier_name = awards[0].get('suppliers', [{}])[0].get('name', 'N/A') if awards else 'N/A'
    
    contracts_value_amount = record.get('contracts', [{}])[0].get('value', {}).get('amount', 'N/A')
    
    date = record.get('date', 'N/A')
    
    # Imprimir campos y valores
   # print(f"ID: {record_id}")
   # print(f"Buyer Name: {buyer_name}")
   # print(f"Awards Description: {awards_description}")
   # print(f"Awards Supplier Name: {awards_supplier_name}")
   # print(f"Contracts Value Amount: {contracts_value_amount}")
   # print(f"Date: {date}")
   # print("\n" + "=" * 80 + "\n")  # Separador visual entre registros

# Abrir el archivo y leer los registros
with open(file_path, 'r', encoding='utf-8') as file:
    # Cargar el contenido JSON
    data = json.load(file)

    # Mostrar la cantidad total de registros
    total_records = len(data)
    print(f"Total de Registros: {total_records}")
    
    # Crear una lista para almacenar los valores únicos de buyer_name
    unique_buyer_names = set()

    # Iterar sobre cada registro y mostrar campos específicos y valores
    for record in data:
        print_specific_fields(record)
        
        # Agregar el valor de buyer_name a la lista de valores únicos
        buyer_name = record.get('buyer', {}).get('name')
        if buyer_name:
            unique_buyer_names.add(buyer_name)

    # Mostrar los valores únicos de buyer_name
    # print(f"\nValores Únicos de buyer_name: {list(unique_buyer_names)}")
    
    # Mostrar los valores únicos de buyer_name con saltos de línea
    print(f"\nValores Únicos de buyer_name:")
    for name in unique_buyer_names:
        print(name)