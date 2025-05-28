<template>
  <v-card class="mt-5 pa-4">
    <v-card-title>Analisar Nova Licitação</v-card-title>
    <v-card-text>
      <v-text-field label="ID da Licitação" v-model="licitacaoId"></v-text-field>
      <v-textarea label="Descrição da Licitação" v-model="descricao"></v-textarea>
      <v-btn color="primary" @click="startAnalysis" :loading="loading">Iniciar Análise</v-btn>

      <v-alert v-if="message" :type="messageType" class="mt-4">{{ message }}</v-alert>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const licitacaoId = ref('');
const descricao = ref('');
const loading = ref(false);
const message = ref('');
const messageType = ref('info');

const startAnalysis = async () => {
  loading.value = true;
  message.value = '';

  try {
    const response = await axios.post('http://localhost:8000/api/licitacoes/analyze', {
      licitacao_id: licitacaoId.value,
      description: descricao.value,
    });
    message.value = response.data.message;
    messageType.value = 'success';
  } catch (error) {
    console.error('Erro ao iniciar análise:', error);
    message.value = 'Erro ao iniciar análise. Verifique o console.';
    messageType.value = 'error';
  } finally {
    loading.value = false;
  }
};
</script>