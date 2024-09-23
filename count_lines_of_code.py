import os
import re

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == '')
    
    # Contar comentarios en Python, HTML y CSS
    comment_lines = sum(
        1 for line in lines 
        if re.match(r'^\s*#', line) or 
           re.match(r'^\s*//', line) or 
           re.match(r'^\s*<!--', line) or 
           re.match(r'^\s*\/\*', line) or 
           re.match(r'^\s*\*', line) or 
           re.match(r'^\s*\*\/', line)
    )
    
    return total_lines, blank_lines, comment_lines

def count_lines_of_code(directory):
    result = {
        'py': {'total': 0, 'blank': 0, 'comments': 0},
        'html': {'total': 0, 'blank': 0, 'comments': 0},
        'css': {'total': 0, 'blank': 0, 'comments': 0}
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.html', '.css')):
                file_path = os.path.join(root, file)
                total, blank, comments = count_lines(file_path)
                
                if file.endswith('.py'):
                    result['py']['total'] += total
                    result['py']['blank'] += blank
                    result['py']['comments'] += comments
                elif file.endswith('.html'):
                    result['html']['total'] += total
                    result['html']['blank'] += blank
                    result['html']['comments'] += comments
                elif file.endswith('.css'):
                    result['css']['total'] += total
                    result['css']['blank'] += blank
                    result['css']['comments'] += comments

    return result

# Cambia el directorio para probar diferentes proyectos
project_directory = 'R:\\programacion\\python\\python\\Programas creados.py\\Repositorios\\To-Do-App'
result = count_lines_of_code(project_directory)

print(f"Python - Total lines of code: {result['py']['total']}, Blank lines: {result['py']['blank']}, Comment lines: {result['py']['comments']}")
print(f"HTML - Total lines of code: {result['html']['total']}, Blank lines: {result['html']['blank']}, Comment lines: {result['html']['comments']}")
print(f"CSS - Total lines of code: {result['css']['total']}, Blank lines: {result['css']['blank']}, Comment lines: {result['css']['comments']}")
