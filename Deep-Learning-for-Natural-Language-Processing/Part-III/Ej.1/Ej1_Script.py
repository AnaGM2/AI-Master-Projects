import praw
import json
import os
import re

# Ruta base para guardar los archivos
ruta_base = r'.\Threads'

# Credenciales de la API de Reddit
reddit = praw.Reddit(client_id='Xn-b5v-4Xof1H5CsGCOF_g',
                     client_secret='rvY41h6nkC53avQB2blMmGexMInyJQ',
                     user_agent='script:DLpPLN-Murcia-2025-AyJ (by u/malatuni99)')

# Lista de subreddits de donde se obtendrán los hilos
subreddit_names = ['Cooking', 'Fitness', 'LetsTalkMusic', 'AskPhysics', 'preppers',
                   'TravelHacks', 'AskHistorians', 'askpsychology', 'askphilosophy', 'nosleep']

# Función para limpiar nombres de archivos
def limpiar_nombre_archivo(nombre):
    return re.sub(r'[<>:"/\\|?*]', '_', nombre)[:50]  # Reemplaza caracteres no válidos y limita longitud

# Función para obtener los hilos de un subreddit
def get_threads(subreddit_name, limit, max_comments):
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.top(limit=limit)
    results = []

    for post in posts:
        post.comments.replace_more(limit=0)
        comments = post.comments.list()[:max_comments]
        comments_list = []

        for comment in comments:
            comments_list.append({
                'author': comment.author.name if comment.author else 'Deleted',
                'body': comment.body,
                'score': comment.score,
                'date': comment.created_utc
            })

        # Verificar si el hilo tiene descripción
        description = post.selftext if post.selftext else None  # Si no tiene descripción, ponemos None

        # Si el hilo tiene descripción, lo añadimos
        if description:
            results.append({
                'flair': post.link_flair_text if post.link_flair_text else 'No Flair',
                'title': post.title,
                'author': post.author.name if post.author else 'Deleted',
                'score': post.score,
                'date': post.created_utc,
                'description': post.selftext,
                'comments': comments_list
            })

    return results

# Contador para el total de hilos cargados
num_threads = 0

# Descargar y guardar los hilos en carpetas separadas
for subreddit_name in subreddit_names:
    threads = get_threads(subreddit_name, limit=20, max_comments=20)
    carpeta_subreddit = os.path.join(ruta_base, subreddit_name)
    os.makedirs(carpeta_subreddit, exist_ok=True)

    # Contar el número de hilos que se van a guardar
    num_threads += len(threads)

    for idx, post in enumerate(threads, start=1):
        safe_title = limpiar_nombre_archivo(post['title'])  # Limpia el título para usarlo como nombre de archivo
        archivo_path = os.path.join(carpeta_subreddit, f'{safe_title}_thread_{idx}.json')

        print(f"Guardando archivo: {archivo_path}")
        with open(archivo_path, 'w', encoding='utf-8') as f:
            json.dump(post, f, indent=4, ensure_ascii=False)

# Mostrar el número total de hilos cargados
print(f"Se han cargado un total de {num_threads} hilos.")

