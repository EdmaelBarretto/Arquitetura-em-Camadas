"""
Interface do Repositório de Usuários.

Define o CONTRATO que qualquer repositório de usuários deve cumprir.
Aplicação do DIP: módulos de alto nível dependem desta abstração,
não de implementações concretas.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from dominio.usuario import Usuario


class InterfaceRepositorioUsuario(ABC):
    """Abstração que define o contrato do repositório de usuários."""

    @abstractmethod
    def salvar(self, usuario: Usuario) -> Usuario:
        """Salva um novo usuário e retorna com ID gerado."""
        ...

    @abstractmethod
    def buscar_por_id(self, usuario_id: int) -> Optional[Usuario]:
        """Busca usuário pelo ID. Retorna None se não encontrar."""
        ...

    @abstractmethod
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca usuário pelo e-mail. Retorna None se não encontrar."""
        ...

    @abstractmethod
    def listar_todos(self) -> List[Usuario]:
        """Retorna lista com todos os usuários."""
        ...

    @abstractmethod
    def atualizar(self, usuario: Usuario) -> Usuario:
        """Atualiza os dados de um usuário existente."""
        ...

    @abstractmethod
    def deletar(self, usuario_id: int) -> bool:
        """Remove um usuário pelo ID. Retorna True se removeu."""
        ...