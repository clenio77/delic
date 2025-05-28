<template>
  <v-card class="mt-5 pa-4">
    <v-card-title>Relatórios das Análises</v-card-title>
    <v-card-text>
      <v-list>
        <v-list-item v-for="report in reports" :key="report.id">
          <v-list-item-title>Análise da Licitação {{ report.licitacao_id }}</v-list-item-title>
          <v-list-item-subtitle>Status: {{ report.status }}</v-list-item-subtitle>
          <v-list-item-subtitle v-if="report.suggested_price">Preço Sugerido: R$ {{ report.suggested_price }}</v-list-item-subtitle>
          <v-list-item-subtitle v-if="report.spec_analysis">Análise de Especificações: {{ report.spec_analysis }}</v-list-item-subtitle>
        </v-list-item>
        <v-list-item v-if="reports.length === 0">Nenhum relatório disponível ainda.</v-list-item>
      </v-list>
      <v-btn @click="fetchReports" class="mt-3">Atualizar Relatórios</v-btn>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const reports = ref([]);

const fetchReports = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/reports');
    reports.value = response.data;
  } catch (error) {
    console.error('Erro ao buscar relatórios:', error);
  }
};

onMounted(fetchReports);
</script>