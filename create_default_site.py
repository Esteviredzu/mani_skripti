import os

def create_project(project_name):
    project_dir = os.path.join(os.getcwd(), project_name)
    templates_dir = os.path.join(project_dir, 'templates')
    index_file = os.path.join(templates_dir, 'index.html')
    styles_file = os.path.join(templates_dir, 'styles.css')

    try:
        os.makedirs(templates_dir)
        print(f"Директория '{templates_dir}' успешно создана")

        with open(index_file, 'w') as file:
            file.write("""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link rel="stylesheet" href="styles.css">
            </head>
            <body>
                <div class="layout">
                    <header>header</header>
                    <main>main</main>
                    <footer>footer</footer>
                </div>
            </body>
            </html>""")
        print(f"Файл '{index_file}' успешно создан")

        with open(styles_file, 'w') as file:
            file.write("""body {
                margin: 0;
            }
            
            .layout {
                display: flex;
                flex-direction: column;
                height: 100vh;
            }
            
            header {
                height: 80px;
                background-color: bisque;
                flex-shrink: 0;
            }
            
            main {
                background-color: aliceblue;
                flex-grow: 1;
            }
            
            footer {
                height: 100px;
                background-color: blueviolet;
                flex-shrink: 0;
            }""")
        print(f"Файл '{styles_file}' успешно создан")

        print(f"Проект '{project_name}' успешно создан")
    except OSError as error:
        print(f"Ошибка при создании проекта '{project_name}': {error}")

if __name__ == "__main__":
    project_name = input("Введите имя проекта: ")
    create_project(project_name)
