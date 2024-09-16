// Executa a função quando o documento HTML estiver totalmente carregado
$(document).ready(function() {
    // Adiciona um ouvinte de evento para o formulário com o ID 'form-usuarios' ao ser submetido
    $('#form-usuarios').on('submit', function(event) {
        // Previne o comportamento padrão do formulário (que seria recarregar a página)
        event.preventDefault();

        // Obtém os valores dos campos do formulário
        const quantidade = $('#quantidade').val(); // Quantidade de usuários a serem gerados
        const genero = $('#genero').val();         // Gênero selecionado ('male', 'female' ou 'both')
        const dominio = $('#dominio').val();       // Domínio de e-mail personalizado fornecido pelo usuário

        // Remove quaisquer classes de alerta e limpa a mensagem anterior
        $('#mensagem').removeClass('d-none alert-success alert-danger').text('');

        // Faz uma requisição AJAX para o servidor Flask
        $.ajax({
            // URL do endpoint no servidor que processará a requisição
            url: '/gerar_usuarios',
            // Método HTTP utilizado para a requisição
            method: 'POST',
            // Dados que serão enviados ao servidor
            data: {
                quantidade: quantidade,
                genero: genero,
                dominio: dominio
            },
            // Função a ser executada se a requisição for bem-sucedida
            success: function(data) {
                // Limpa a lista de usuários exibida anteriormente
                $('#lista-usuarios').empty();

                // Itera sobre cada usuário retornado pelo servidor
                data.forEach(function(usuario) {
                    // Cria um item de lista contendo as informações do usuário
                    const item = `<li class="list-group-item">
                        <strong>${usuario.nome} ${usuario.sobrenome}</strong>
                        Email: ${usuario.email}<br>
                        Username: ${usuario.username}<br>
                        Telefone: ${usuario.telefone}<br>
                        Data de Nascimento: ${usuario.data_nascimento}<br>
                        Endereço: ${usuario.endereco.rua}, ${usuario.endereco.cidade} - ${usuario.endereco.estado}, CEP: ${usuario.endereco.cep}
                    </li>`;
                    // Adiciona o item criado à lista de usuários no HTML
                    $('#lista-usuarios').append(item);
                });
            },
            // Função a ser executada se ocorrer um erro na requisição
            error: function(xhr) {
                // Obtém a mensagem de erro retornada pelo servidor ou define uma mensagem padrão
                const erro = xhr.responseJSON ? xhr.responseJSON.erro : 'Erro desconhecido';
                // Exibe a mensagem de erro na página, adicionando classes para formatação
                $('#mensagem').addClass('alert alert-danger').text(erro).removeClass('d-none');
            }
        });
    });
});
