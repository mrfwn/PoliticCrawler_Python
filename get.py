import requests
urlBase = "http://web.transparencia.pe.gov.br/pentaho/api/repos/%3Apublic%3AOpenReports%3APortal_Producao%3APainel_Despesas_Detalhamento%3APainel_Despesa_Detalhamento.wcdf/generatedContent"
urlPost = "http://web.transparencia.pe.gov.br/pentaho/plugin/cda/api/doQuery?"
session = requests.session()
session.headers = {'User-Agent': 'Mozilla/5.0'}
resp = session.get(urlBase)
data ={
    'paramlimit_': 200,
    'paramoffset_': 0,
    'parampara_ano': 2018,
    'parampara_ug': 0,
    'parampara_empenho': "",
    'parampara_categoria': 0,
    'parampara_grupo': 0,
    'parampara_orgao': 314,
    'parampara_modalidade': 0,
    'parampara_elemento': 0,
    'paramativa': "",
    'parampara_funcao': "%%",
    'parampara_acao': "%%",
    'parampesquisa_': "",
    'parampesquisa_emp': "",
    'parampesquisa_obs': "",
    'parampara_ano_emp': 0,
    'parampara_subfuncao': "%%",
    'parampara_programa': "%%",
    'parampara_subacao': "%%",
    'parampara_fonte': "%%",
    'path': "/public/OpenReports/Portal_Producao/Painel_Despesas_Detalhamento/Painel_Despesa_Detalhamento.cda",
    'dataAccessId': "select_tabela_empenho",
    'outputIndexId': 1,
    'pageSize': 0,
    'pageStart': 0,
    'sortBy': "",
    'paramsearchBox': ""
}
resp2 = session.post(urlPost, data = data)

print(resp2)
print(resp2.content.decode("UTF-8","ignore"))
