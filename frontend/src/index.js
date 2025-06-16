import React from 'react';
import ReactDOM from 'react-dom/client'; // Importa o cliente do ReactDOM
import './index.css'; // Você pode criar este arquivo para estilos globais
import App from './App'; // Importa o componente App

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
