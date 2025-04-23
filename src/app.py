
usuarios = []

def criar_usuario(nome, email, senha, cpf):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        return "CPF já cadastrado."
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'cpf': cpf
          
    }
    usuarios.append(usuario)
    return "Usuário criado com sucesso."

def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def deletar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            return "Usuário removido com sucesso."
    return "Usuário não encontrado."
