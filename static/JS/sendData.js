$(document).ready(function() {
    // Inicialização dos select2
    $('#bioma').select2({
        placeholder: "Selecione uma ou mais opções",
        allowClear: true,
        width: '100%' // Ajusta a largura do select2 para 100%
    });

    $('#area_especial').select2({
        placeholder: "Selecione uma ou mais opções",
        allowClear: true,
        width: '100%' // Ajusta a largura do select2 para 100%
    });

    $('#tipo_unidade').select2({
        placeholder: "Selecione uma ou mais opções",
        allowClear: true,
        width: '100%' // Ajusta a largura do select2 para 100%
    });

    // Carregar estados do IBGE
    $.getJSON('https://servicodados.ibge.gov.br/api/v1/localidades/estados/', function (uf) {
        var options = '<option value="" selected disabled>– Selecione o estado –</option>';
        uf.sort((a, b) => a.nome.localeCompare(b.nome));
        for (var i = 0; i < uf.length; i++) {
            options += '<option data-id="' + uf[i].id + '" value="' + uf[i].nome + '">' + uf[i].nome + '</option>';
        }
        $("select[name='uf']").html(options);
    });

    // Atualizar municípios com base no estado selecionado
    $("select[name='uf']").change(function () {
        if ($(this).val()) {
            const ufSelect = $(this).find("option:selected").attr('data-id');
            $.getJSON('https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + ufSelect + '/municipios', { id: ufSelect }, function (city) {
                var options = '<option value="" disabled selected>– Selecione a cidade –</option>';
                for (var i = 0; i < city.length; i++) {
                    options += '<option value="' + city[i].nome + '">' + city[i].nome + '</option>';
                }
                $("select[name='municipio']").html(options);
            });
        } else {
            $("select[name='municipio']").html('<option value="" disabled selected>– Selecione sua cidade –</option>');
        }
    });
});

// Envia os dados para o backend
$(document).ready(function() {
    $('#filtro-form').on('submit', function(event) {
        event.preventDefault(); // Previne o envio do formulário tradicional

        const dataInicio = $('#data_inicio').val();
        const dataFim = $('#data_fim').val();
        const pais = $('#pais').val();
        const areaEspecial = $('#area_especial').val();
        const uf = $('select[name="uf"]').val();
        const municipio = $('select[name="municipio"]').val();
        const bioma = $('#bioma').val();
        const tipoUnidade = $('#tipo_unidade').val();
        const dominio = $('#dominio').val();

        const filtros = {
            data_inicio: dataInicio,
            data_fim: dataFim,
            pais: pais,
            areaEspecial: areaEspecial,
            uf: uf,
            municipio: municipio,
            bioma: bioma,
            tipoUnidade: tipoUnidade,
            dominio: dominio,
        };

        $.ajax({
            type: 'POST',
            url: '/filtrar',
            contentType: 'application/json',
            data: JSON.stringify(filtros),
            success: function(response) {
                $('#grafico_linhas').html(response.grafico_linhas_html);
                $('#grafico_barras').html(response.grafico_barras_html);
                $('#tabela').html(response.tabela_html);
            },
            error: function(error) {
                console.error('Erro ao consultar:', error);
            }
        });
    });
});
