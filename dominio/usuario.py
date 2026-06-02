"""
Camada de Domínio - Entidade Usuario e regras de negócio puras.

Responsabilidades:
- Definir a estrutura da entidade Usuario
- Implementar validações de domínio
- Encapsular comportamentos da entidade
- Garantir invariantes do domínio

NÃO deve conter:
- Dependências de outras camadas
- Código de infraestrutura (banco de dados, APIs)
- Lógica de apresentação
- Detalhes de persistência
"""

import re
from dataclasses import dataclass
from typing import Optional


class UsuarioInvalidoError(Exception):
    """Exceção lançada quando dados do usuário são inválidos."""
    pass


@dataclass
class Usuario:
    nome: str
    email: str
    id: Optional[int] = None
    ativo: bool = True
    telefone: Optional[str] = None

    def __post_init__(self):
        self._validar_nome(self.nome)
        self._validar_email(self.email)
        if self.telefone is not None:
            self._validar_telefone(self.telefone)

    @staticmethod
    def _validar_nome(nome: str) -> None:
        if not nome or not nome.strip():
            raise UsuarioInvalidoError("Nome não pode ser vazio")
        nome_limpo = nome.strip()
        if len(nome_limpo) < 2:
            raise UsuarioInvalidoError("Nome deve ter pelo menos 2 caracteres")
        if len(nome_limpo) > 100:
            raise UsuarioInvalidoError("Nome deve ter no máximo 100 caracteres")

    @staticmethod
    def _validar_email(email: str) -> None:
        if not email or not email.strip():
            raise UsuarioInvalidoError("Email não pode ser vazio")
        email_limpo = email.strip().lower()
        if len(email_limpo) > 255:
            raise UsuarioInvalidoError("Email deve ter no máximo 255 caracteres")
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao_email, email_limpo):
            raise UsuarioInvalidoError("Formato de email inválido")

    @staticmethod
    def _validar_telefone(telefone: str) -> None:
        if telefone is None:
            return
        apenas_numeros = re.sub(r'\D', '', telefone)
        if len(apenas_numeros) < 10 or len(apenas_numeros) > 11:
            raise UsuarioInvalidoError("Telefone deve ter 10 ou 11 dígitos")

    def atualizar_nome(self, novo_nome: str) -> None:
        self._validar_nome(novo_nome)
        self.nome = novo_nome.strip()

    def atualizar_email(self, novo_email: str) -> None:
        self._validar_email(novo_email)
        self.email = novo_email.strip().lower()

    def ativar(self) -> None:
        self.ativo = True

    def desativar(self) -> None:
        self.ativo = False

    def esta_ativo(self) -> bool:
        return self.ativo

    def __str__(self) -> str:
        status = "ativo" if self.ativo else "inativo"
        return f"Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', {status})"

    def __repr__(self) -> str:
        return (f"Usuario(id={self.id}, nome='{self.nome}', "
                f"email='{self.email}', ativo={self.ativo})")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Usuario):
            return False
        return self.id is not None and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id) if self.id else hash((self.nome, self.email))