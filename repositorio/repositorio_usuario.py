"""
Camada de Repositório - Acesso a dados de usuários.

Responsabilidades:
- Abstrair acesso ao banco de dados
- Implementar operações CRUD
- Converter entre entidades de domínio e registros de BD
- Executar queries SQL

NÃO deve conter:
- Lógica de negócio
- Regras de validação de domínio
- Formatação de respostas HTTP
- Lógica de orquestração
"""

from typing import Optional, List
from dominio.usuario import Usuario
from dados.db import obter_conexao
# ✅ DIP: importa a abstração para que RepositorioUsuario cumpra o contrato
from repositorio.interface_repositorio import InterfaceRepositorioUsuario


# ✅ DIP APLICADO: herda da interface, garantindo que implementa o contrato
class RepositorioUsuario(InterfaceRepositorioUsuario):
    
    def salvar(self, usuario: Usuario) -> Usuario:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                """
                INSERT INTO usuarios (nome, email, ativo, telefone)
                VALUES (?, ?, ?, ?)
                """,
                (usuario.nome, usuario.email, usuario.ativo, usuario.telefone)
            )
            
            usuario_id = cursor.lastrowid
            conexao.commit()
            usuario.id = usuario_id
            return usuario
            
        except Exception as e:
            conexao.rollback()
            raise Exception(f"Erro ao salvar usuário: {str(e)}")
        finally:
            cursor.close()
    
    def buscar_por_id(self, usuario_id: int) -> Optional[Usuario]:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                """
                SELECT id, nome, email, ativo, telefone
                FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,)
            )
            
            linha = cursor.fetchone()
            
            if linha:
                return self._converter_linha_para_usuario(linha)
            
            return None
            
        finally:
            cursor.close()
    
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                """
                SELECT id, nome, email, ativo, telefone
                FROM usuarios
                WHERE email = ?
                """,
                (email.lower(),)
            )
            
            linha = cursor.fetchone()
            
            if linha:
                return self._converter_linha_para_usuario(linha)
            
            return None
            
        finally:
            cursor.close()
    
    def listar_todos(self) -> List[Usuario]:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                """
                SELECT id, nome, email, ativo, telefone
                FROM usuarios
                ORDER BY nome
                """
            )
            
            linhas = cursor.fetchall()
            
            return [self._converter_linha_para_usuario(linha) for linha in linhas]
            
        finally:
            cursor.close()
    
    def atualizar(self, usuario: Usuario) -> Usuario:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                """
                UPDATE usuarios
                SET nome = ?, email = ?, ativo = ?
                WHERE id = ?
                """,
                (usuario.nome, usuario.email, usuario.ativo, usuario.id)
            )
            
            conexao.commit()
            return usuario
            
        except Exception as e:
            conexao.rollback()
            raise Exception(f"Erro ao atualizar usuário: {str(e)}")
        finally:
            cursor.close()
    
    def deletar(self, usuario_id: int) -> bool:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        try:
            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,)
            )
            
            linhas_afetadas = cursor.rowcount
            conexao.commit()
            
            return linhas_afetadas > 0
            
        except Exception as e:
            conexao.rollback()
            raise Exception(f"Erro ao deletar usuário: {str(e)}")
        finally:
            cursor.close()
    
    @staticmethod
    def _converter_linha_para_usuario(linha: tuple) -> Usuario:
        usuario_id, nome, email, ativo, telefone = linha
        
        usuario = Usuario(
            nome=nome,
            email=email,
            ativo=bool(ativo),
            telefone=telefone
        )
        usuario.id = usuario_id
        
        return usuario