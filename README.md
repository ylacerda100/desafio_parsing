# desafio_parsing


# Teste migração de dados 

O objetivo é baixar os dados de CNPJ disponibilizados pela receita, extrair, fazer o parse, disponibilizar em um banco de dados e criar uma API para consulta.   

### 1 - Crie um robô que baixe um ou mais arquivos de CNPJ

Os arquivos podem ser baixados em https://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj 

	exemplo:  
		- http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_01.zip 
		- http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_02.zip 
 
obs.: recomendamos deixar esse item para o final do projeto pois o download é lento, por isso estamos disponibilizando uma versão baixada para que você faça as etapas abaixo. 


### 2 - Extrair o arquivo zip 
 

### 3 - Ler o arquivo e fazer o parser 

	obs.: Faça o parser apenas dos campos abaixo: 

	- Dados empresas (LAYOUT PRINCIPAL)
		- CNPJ
		- IDENTIFICADOR MATRIZ/FILIAL 
		- RAZÃO SOCIAL/NOME EMPRESARIAL
		- NOME FANTASIA 
		- SITUAÇÃO CADASTRAL 
		- DATA SITUACAO CADASTRAL 
		- CEP 
	- Sócios (LAYOUT SOCIOS) 
		- IDENTIFICADOR DE SOCIO 
		- NOME SOCIO (NO CASO PF) OU RAZÃO SOCIAL (NO CASO PJ) 
		- CNPJ/CPF DO SÓCIO   

Documento com layout do arquivo http://200.152.38.155/CNPJ/LAYOUT_DADOS_ABERTOS_CNPJ.pdf	 

### 4 - Inserir os dados em um banco de dados MongoDB (ou de sua preferência) 

### 5 - Crie uma API que ao enviar o número do CNPJ retorne as informações correspondente em JSON 

	exemplo:
		request: http://localhost/cnpj/00000000000191 
		response: Contém os dados do CNPJ buscado no formato JSON
