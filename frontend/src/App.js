import React, { useState, useEffect } from 'react'; // Importa useState e useEffect
import './styles.css'; // Importa o arquivo CSS
import LicitacaoCard from './components/LicitacaoCard'; // Importa o componente LicitacaoCard

function App() {
  const [licitacoes, setLicitacoes] = useState([]); // Estado para armazenar as licitações
  const [loading, setLoading] = useState(true); // Estado para indicar se está carregando
  const [error, setError] = useState(null); // Estado para armazenar erros

  // useEffect para buscar dados da API ao montar o componente
  useEffect(() => {
    // Novo endpoint para buscar as licitações
    const API_URL = '/api/licitacoes';

    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          // Lança um erro se a resposta não for 2xx
          throw new Error(`Erro HTTP! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setLicitacoes(data); // Atualiza o estado com os dados da API
        setLoading(false); // Define loading para false
      })
      .catch(error => {
        setError(error); // Armazena o erro no estado
        setLoading(false); // Define loading para false mesmo em caso de erro
        console.error("Erro ao buscar licitações:", error);
      });
  }, []); // O array vazio [] garante que este useEffect roda apenas uma vez ao montar o componente

  // Renderização condicional baseada no estado (carregando, erro, dados)
  if (loading) {
    return <div className="App">Carregando licitações...</div>;
  }

  if (error) {
    return (
      <div className="App">
        <h1>Erro ao carregar licitações:</h1>
        <p>{error.message}</p>
        {/* Opcional: Exibir dados de exemplo em caso de erro */}
        {/* <div className="licitacoes-list">
          {licitacoesDeExemplo.map(licitacao => (
            <LicitacaoCard key={licitacao.id} licitacao={licitacao} />
          ))}
        </div> */}
      </div>
    );
  }

  // Se não está carregando e não há erro, exibe a lista de licitações
  return (
    <div className="App">
      <header className="App-header">
        <h1>Lista de Licitações</h1>
      </header>
      <div className="licitacoes-list">
        {/* Renderiza os cards usando os dados do estado 'licitacoes' */}
        {licitacoes.length > 0 ? (
          licitacoes.map(licitacao => (
            <LicitacaoCard key={licitacao.id || licitacao.titulo} licitacao={licitacao} /> // Usar um id único se disponível, senão o título
          ))
        ) : (
          <p>Nenhuma licitação encontrada.</p>
        )}
      </div>
    </div>
  );
}

export default App;
