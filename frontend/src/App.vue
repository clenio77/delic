<template>
  <v-app>
    <v-app-bar app color="primary">
      <v-toolbar-title>Sistema de Agentes DELIC</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/">Início</v-btn>
      <v-btn text to="/analyze">Analisar Licitação</v-btn>
      <v-btn text to="/reports">Relatórios</v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
// Sem lógica específica aqui por enquanto, apenas a estrutura de navegação.
</script>