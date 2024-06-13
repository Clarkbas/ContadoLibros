import matplotlib.pyplot as plt


def generateBarChart(labels, values):
    fig, ax = plt.subplots()

    ax.bar(labels, values, color=['blue', 'green', 'red', 'purple', 'orange'])

    ax.set_xlabel('Géneros')
    ax.set_ylabel('Cantidad de Libros')
    ax.set_title('Cantidad de Libros por Género')
    plt.show()

if __name__ == '__main__':
    labels = ['Histórico', 'Ficción', 'Ficción contemporánea', 'Misterio', 'Fantasía', 'Horror', 'Distopía', 'Post-apocalíptico', 'Aventura', 'Épico', 'Ficción literaria', 'Ciencia ficción', 'Romance']
    values = [4, 5, 2, 0, 5, 1, 15, 1, 2, 1, 1, 5, 3]
    generateBarChart(labels, values)