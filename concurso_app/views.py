from django.shortcuts import render, redirect
from .models import Concurso, Examinador, Prova, Candidato, Nota


def cadastro_view(request):
    context = {}
    if request.method == "POST":
        # Capturar dados do formulário na página 1_cadastro.html
        numero_processo = request.POST.get('numero_processo')
        area_concurso = request.POST.get('area_concurso')
        orgao_realizador = request.POST.get('orgao_realizador')
        numero_provas = int(request.POST.get('numero_provas'))

        # Criar o objeto Concurso e salvar no banco de dados
        concurso = Concurso.objects.create(
            numero_processo=numero_processo,
            area_concurso=area_concurso,
            orgao_realizador=orgao_realizador
        )

        # Capturar e criar Examinadores
        for i in range(1, 6):  # Assumindo 5 examinadores como no exemplo
            nome_examinador = request.POST.get(f'examinador_{i}')
            if nome_examinador:
                Examinador.objects.create(nome=nome_examinador, concurso=concurso)

        # Redirecionar para a página de cadastro de provas passando o número de provas via URL ou sessão
        request.session['numero_provas'] = numero_provas
        request.session['concurso_id'] = concurso.id  # Armazena o ID do concurso na sessão
        return redirect('provas')  # Nome da URL configurado para a view provas_view

    # Defina o range de examinadores
    context['examinadores_range'] = range(5)

    return render(request, '1_cadastro.html', context)


def provas_view(request):
    # Verifica o número de provas na sessão
    numero_provas = request.session.get('numero_provas', 1)  # Padrão 1 prova se não houver na sessão
    concurso_id = request.session.get('concurso_id')  # Recupera o ID do concurso da sessão
    concurso = Concurso.objects.get(id=concurso_id)  # Obtém o concurso correspondente

    provas_list = [{'id': i} for i in range(1, numero_provas + 1)]  # Lista de dicionários para as provas

    # Contexto a ser passado para o template
    context = {
        'provas_list': provas_list,
    }

    if request.method == "POST":
        # Lógica para processar o formulário de provas
        # Exemplo de captura de dados:
        for prova in provas_list:
            nome = request.POST.get(f'nome_prova_{prova["id"]}')
            eliminatoria = request.POST.get(f'eliminatoria_{prova["id"]}') == 'sim'
            peso = float(request.POST.get(f'peso_{prova["id"]}'))
            num_pessoas = int(request.POST.get(f'num_pessoas_{prova["id"]}'))

            # Criar e salvar a prova no banco de dados
            Prova.objects.create(
                concurso=concurso,
                nome=nome,
                eliminatoria=eliminatoria,
                peso=peso,
                num_pessoas=num_pessoas
            )

        # Redireciona para a próxima etapa, que é a página 3_planilha
        return redirect('planilha', concurso_id=concurso.id)  # Use o ID do concurso real

    return render(request, '2_provas.html', context)


def planilha_view(request, concurso_id):
    concurso = Concurso.objects.get(id=concurso_id)
    return render(request, '3_planilha.html', {'concurso': concurso})


def relatorio_view(request, concurso_id):
    concurso = Concurso.objects.get(id=concurso_id)
    return render(request, '4_relatorio.html', {'concurso': concurso})


