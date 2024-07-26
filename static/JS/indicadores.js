$( '#multiple-select-clear-field' ).select2( {
  theme: "bootstrap-5",
  width: $( this ).data( 'width' ) ? $( this ).data( 'width' ) : $( this ).hasClass( 'w-100' ) ? '100%' : 'style',
  placeholder: $( this ).data( 'placeholder' ),
  closeOnSelect: false,
  allowClear: true,
} );

// Função para limapr os filtros
function limparFiltros() {
  document.location.reload(true);
}

// Função para mostrar as unidades da área especial
function mostrarUnidades() {
  var areaEspecial = $('#area_especial').val();
  var unidadeConservacao = document.getElementById('unidade-conservacao');
  if (areaEspecial.includes('is_unidade_conservacao')) {
      unidadeConservacao.style.display = 'block';
  } else {
      unidadeConservacao.style.display = 'none';
  }
}

//Função que inicia o preloader durante a pesquisa
document.getElementById('consultar').addEventListener('click', function (){
  document.getElementById('preloader').style.display = 'flex';
  fetch('/filtrar')
    .then(response => response.json()) //o tipo aqui é o tipo de dado retornado na consulta
    .then(data => {
      renderGraph(data);
      document.getElementById('preloader').style.display = 'none';
    })

    .catch(error => {
      console.error('Erro na busca de dados: ', error);
      document.getElementById('preloader').style.display = 'none';
    });
});

function renderGraph(data) {
  const grafico_linhas = document.getElementById('grafico_linhas');

  setTimeout(() => {
    grafico_linhas.style.display = 'none';
}, 1000);
}