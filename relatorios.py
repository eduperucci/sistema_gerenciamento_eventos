from dados import lista_eventos, lista_de_participantes
from util import limpar_tela, enter_continuar

def participantes_por_tema():
    limpar_tela()
    print("\n---PARTICIPANTES POR TEMA---")
    if not lista_eventos or not lista_de_participantes:
        print("Nenhum evento ou participante cadastrado.")
        return
    
    temas = {}
    for evento in lista_eventos:
        tema = evento['tema']
        if tema not in temas:
            temas[tema] = []
    
    for participante in lista_de_participantes:
        eventos = participante.get('evento_cadastrado')
        if isinstance(eventos, dict):
            eventos = [eventos]
        elif not isinstance(eventos, list):
            eventos = []
        for ev in eventos:
            tema = ev.get('tema')
            if tema:
                temas.setdefault(tema, []).append(participante)
    
    for tema, participantes in temas.items():
        print(f"\nTema: {tema}")
        if participantes:
            for p in participantes:
                print(f"   CPF: {p['cpf']} | Nome: {p['nome']} | Email: {p['email']}")
        else:
            print("  Nenhum participante inscrito nesse tema.")
    enter_continuar()


def participantes_por_evento():
    limpar_tela()
    print("\n---PARTICIPANTES POR EVENTO---")
    if not lista_eventos or not lista_de_participantes:
        print("Nenhum evento ou participante cadastrado.")
        return
    
    eventos_dict = {evento['id']: evento for evento in lista_eventos}
    participantes_evento = {evento['id']: [] for evento in lista_eventos}
    
    for participante in lista_de_participantes:
        eventos = participante.get('evento_cadastrado')
        if isinstance(eventos, dict):
            eventos = [eventos]
        elif not isinstance(eventos, list):
            eventos = []
        for ev in eventos:
            eid = ev.get('id')
            if eid in participantes_evento:
                participantes_evento[eid].append(participante)
    
    for eid, participantes in participantes_evento.items():
        evento = eventos_dict[eid]
        print(f"\nEvento: {evento['nome']} (Tema: {evento['tema']}, Data: {evento['data']})")
        if participantes:
            for p in participantes:
                print(f"  CPF: {p['cpf']} | Nome: {p['nome']} | Email: {p['email']}")
        else:
            print("Nenhum participante inscrito nesse evento.")
    enter_continuar()


    