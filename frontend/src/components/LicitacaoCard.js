import React from 'react';
import '../styles.css'; // Pode ser necessário ajustar o caminho se o CSS for mais específico

function LicitacaoCard({ licitacao }) {
  // Verifica se o objeto licitacao existe antes de tentar acessar suas propriedades
  if (!licitacao) {
    return <div>Nenhuma licitação disponível.</div>;
  }

  return (
    <div className="licitacao-card">
      <h3>{licitacao.titulo || 'Sem Título'}</h3>
      <p><strong>Status:</strong> {licitacao.status || 'Não especificado'}</p>
      <p><strong>Data de Publicação:</strong> {licitacao.dataPublicacao || 'Não especificada'}</p>
      <p><strong>Órgão:</strong> {licitacao.orgao || 'Não especificado'}</p>
      {/* Adicione mais detalhes da licitação conforme necessário */}
      <a href={licitacao.link || '#'} target="_blank" rel="noopener noreferrer">Ver Detalhes</a>
    </div>
  );
}

export default LicitacaoCard;
