function mostrarGrafico(tipo) {
    var containerBarras = document.getElementById('container_barras');
    var containerLinhas = document.getElementById('container_linhas');

    if (tipo === 'barras') {
        containerBarras.classList.remove('hidden');
        containerLinhas.classList.add('hidden');
    } else if (tipo === 'linhas') {
        containerBarras.classList.add('hidden');
        containerLinhas.classList.remove('hidden');
    } else if (tipo === 'ambos') {
        containerBarras.classList.remove('hidden');
        containerLinhas.classList.remove('hidden');
    }
}

// Chama a função mostrarGrafico no carregamento da página para exibir o gráfico de barras por padrão
document.addEventListener('DOMContentLoaded', function() {
    mostrarGrafico('barras');
});