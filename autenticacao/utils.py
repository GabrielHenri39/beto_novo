import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(password, confirm_password, request=None):
    """
    Verifica se a senha é válida e adiciona mensagens para o usuário.

    Parâmetros:
    password -- A senha a ser validada
    confirm_password -- A confirmação da senha
    request -- O objeto request da view

    Retorna:
    True se a senha for válida, False caso contrário
    """

    if not request:
        return False

    if not re.match("^.{8,}$", password):
        messages.add_message(request, constants.ERROR,'A senha deve ter pelo menos 8 caracteres.')
        return False

    if not password.strip() == confirm_password.strip():
        messages.add_message(request,constants.ERROR, 'As senhas não conferem.')
        return False

    if not re.search(r'[A-Z]', password.strip()):
        messages.add_message(request, constants.ERROR,'A senha deve conter pelo menos uma letra maiúscula.')
        return False

    if not re.search(r'[a-z]', password.strip()):
        messages.add_message(request, constants.ERROR,'A senha deve conter pelo menos uma letra minúscula.')
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password.strip()):
        messages.add_message(request, constants.ERROR,'A senha deve conter pelo menos um caractere especial.')
        return False

    if re.match(r'[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}', password.strip()):
        messages.add_message(request, constants.ERROR,'A senha não pode ser uma data de nascimento.')
        return False

    if re.match(r'[0-9]{1,3}[-_ ][0-9]{1,3}[-_ ][0-9]{1,3}', password.strip()):
        messages.add_message(request, constants.ERROR,'A senha não pode ser uma sequência de números.')
        return False

    messages.success(request, 'Senha válida!')
    return True
