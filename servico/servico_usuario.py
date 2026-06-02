"""
Camada de Serviço - Lógica de negócio para gerenciamento de usuários.

Responsabilidades:
- Orquestrar operações de negócio
- Aplicar regras de negócio
- Validar dados de domínio
- Coordenar chamadas ao repositório

NÃO deve conter:
- Código de apresentação (rotas, HTTP)
- Acesso direto ao banco de dados
- Detalhes de infraestrutura
"""

from dominio.usuario import Usuario
# ✅ DIP: depende da ABSTRAÇÃO, não da implementação concreta
from repositorio.interface_repositorio import InterfaceRepositorioUsuario


class ServicoUsuario:
    """
    Serviço responsável pela lógica de negócio de usuários.
    """
    
    def __init__(self, repositorio: InterfaceRepositorioUsuario):
        """
        Inicializa o serviço com suas dependências.
        
        A dependência é recebida via parâmetro (injeção de dependência),
        permitindo trocar a implementação sem alterar esta classe.
        """
        # ✅ DIP APLICADO: dependência injetada via construtor
        self.repositorio = repositorio
    
    def criar_usuario(self, nome: str, email: str, telefone: str = None) -> Usuario:
        """
        Cria um novo usuário aplicando regras de negócio.
        
        Regras de negócio:
        1. Email deve ser único no sistema
        2. Nome e email devem ser válidos (validado pela entidade)
        3. Usuário é criado como ativo por padrão
        
        Args:
            nome: Nome do usuário
            email: Email do usuário
            telefone: Telefone do usuário (opcional)
        
        Returns:
            Usuario: Usuário criado com ID
        
        Raises:
            ValueError: Se email já existe
            UsuarioInvalidoError: Se dados são inválidos
        """
        # Regra de negócio: Email deve ser único
        usuario_existente = self.repositorio.buscar_por_email(email)
        if usuario_existente:
            raise ValueError(f"Email '{email}' já está cadastrado no sistema")
        
        # Criar entidade de domínio (valida dados automaticamente)
        usuario = Usuario(nome=nome, email=email, telefone=telefone)
        
        # Persistir no banco de dados
        usuario_salvo = self.repositorio.salvar(usuario)
        
        return usuario_salvo
    
    def obter_usuario_por_id(self, usuario_id: int) -> Usuario:
        return self.repositorio.buscar_por_id(usuario_id)
    
    def obter_usuario_por_email(self, email: str) -> Usuario:
        return self.repositorio.buscar_por_email(email)
    
    def listar_usuarios(self) -> list[Usuario]:
        return self.repositorio.listar_todos()
    
    def atualizar_usuario(self, usuario_id: int, nome: str = None, 
                         email: str = None) -> Usuario:
        usuario = self.repositorio.buscar_por_id(usuario_id)
        if not usuario:
            return None
        
        if email and email != usuario.email:
            usuario_com_email = self.repositorio.buscar_por_email(email)
            if usuario_com_email:
                raise ValueError(f"Email '{email}' já está cadastrado")
        
        if nome:
            usuario.atualizar_nome(nome)
        if email:
            usuario.atualizar_email(email)
        
        return self.repositorio.atualizar(usuario)
    
    def deletar_usuario(self, usuario_id: int) -> bool:
        usuario = self.repositorio.buscar_por_id(usuario_id)
        if not usuario:
            return False
        
        usuario.desativar()
        self.repositorio.atualizar(usuario)
        
        return True
    
    def reativar_usuario(self, usuario_id: int) -> bool:
        usuario = self.repositorio.buscar_por_id(usuario_id)
        if not usuario:
            return False
        
        usuario.ativar()
        self.repositorio.atualizar(usuario)
        
        return True