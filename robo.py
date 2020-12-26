from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'application/zip,application/download')


navegador = webdriver.Firefox(profile)

navegador.get('https://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj')

arquivo = navegador.find_element_by_xpath(
    '/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/div[5]/div/p[3]/a')

arquivo.click()
