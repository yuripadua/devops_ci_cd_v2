# **Gerador de Fake Users**

Uma aplicação web em Flask que gera usuários fictícios com dados aleatórios para fins educacionais. O projeto demonstra conceitos de desenvolvimento web, testes automatizados e integração contínua (CI/CD) usando GitHub Actions.

---

## **Tabela de Conteúdos**

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Execução da Aplicação](#execução-da-aplicação)
- [Uso](#uso)
  - [Interface Web](#interface-web)
  - [API via Insomnia ou cURL](#api-via-insomnia-ou-curl)
- [Testes Automatizados](#testes-automatizados)
- [Documentação da API](#documentação-da-api)
- [CI/CD com GitHub Actions](#cicd-com-github-actions)
- [Contribuição](#contribuição)
- [Contato](#contato)

---

## **Descrição do Projeto**

Este projeto consiste em uma aplicação web desenvolvida em Flask que permite gerar dados fictícios de usuários. O objetivo é fornecer um exemplo prático para demonstrar conceitos de desenvolvimento de APIs, testes automatizados e pipelines de CI/CD.

---

## **Funcionalidades**

- **Geração de Usuários Aleatórios**:
  - Nome e sobrenome
  - Email com domínios personalizados
  - Endereço completo
  - Telefone
  - Data de nascimento
  - Nome de usuário (username)
- **Parâmetros Personalizados**:
  - Quantidade de usuários a serem gerados
  - Gênero dos usuários (masculino, feminino ou ambos)
  - Domínios de e-mail personalizados
- **Interface Web Amigável**:
  - Formulário interativo usando Bootstrap
  - Exibição dinâmica dos usuários gerados
- **API RESTful**:
  - Endpoint para geração de usuários via requisições HTTP POST
- **Testes Automatizados**:
  - Testes unitários usando pytest
  - Cobertura de código com coverage
- **Documentação da API**:
  - Documentação interativa usando Flasgger (Swagger para Flask)
- **Integração Contínua (CI/CD)**:
  - Pipeline configurado com GitHub Actions
  - Execução de testes automatizados e linting
  - Deploy automatizado para o Render em ambientes de homologação e produção

---

## **Tecnologias Utilizadas**

- **Linguagem**: Python 3.x
- **Framework Web**: Flask
- **Front-end**: HTML5, CSS3, Bootstrap, jQuery
- **Testes**: pytest, coverage
- **Documentação da API**: Flasgger (Swagger)
- **CI/CD**: GitHub Actions
- **Deploy**: [Render](https://render.com/)

---

## **Pré-requisitos**

- Python 3.8 ou superior
- Git (para clonar o repositório)
- Pip (gerenciador de pacotes do Python)
- Ambiente virtual (recomendado)

---

## **Instalação**

### **1. Clonar o Repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
