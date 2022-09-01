from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


class Registration():
    def CT_001():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys(199999)
        elem.send_keys(RETURN)
        self.assertIn("por favor, informe o nome e o sobrenome.") 
        driver.close()

    def CT_002():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("****%^^&&!@@##$")
        elem.send_keys(RETURN)
        self.assertIn("por favor, informe o nome e o sobrenome.") 
        driver.close()

    def CT_003():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        elem.send_keys(RETURN)
        self.assertIn("nome deve ser completo.") 
        driver.close()

    def CT_004():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("<script>alert(`hello world`)</script>")
        elem.send_keys(RETURN)
        self.assertIn("hello world") 
        driver.close()

    def CT_005():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("")
        elem.send_keys(RETURN)
        self.assertIn("campo obrigatório") 
        driver.close()

    def CT_006():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("aaaaa")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_007():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("01/14/2020")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_008():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("32/14/2020")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()
  
    def CT_009():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("32/14/1700")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_010():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("&&/!!/#####")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_011():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x18sc4-3 cXOnMx")
        elem.send_keys("&&/!!/#####")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_012():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x18sc4-3 cXOnMx")
        elem.send_keys("aaaaaaaa")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_013():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x18sc4-3 cXOnMx")
        elem.send_keys("112212333333333333333333333333333333333")
        elem.send_keys(RETURN)
        self.assertIn("Please fill this field") 
        driver.close()

    def CT_014():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys("11221233333333333333333333333333333333211111111111111111111111111111113")
        elem.send_keys(RETURN)
        self.assertIn("precisa ter entre 6 e 20 caracteres") 
        driver.close()

    def CT_015():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys("1")
        elem.send_keys(RETURN)
        self.assertIn("precisa ter entre 6 e 20 caracteres") 
        driver.close()

    def CT_016():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("1")
        elem.send_keys(RETURN)
        self.assertIn("cpf inválido") 
        driver.close()

    def CT_017():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("&&&&&&&&&&&&&")
        elem.send_keys(RETURN)
        self.assertIn("cpf inválido") 
        driver.close()

    def CT_018():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("aaaaaaaaaaaaaaaa")
        elem.send_keys(RETURN)
        self.assertIn("endereço inválido") 
        driver.close()

    def CT_019():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "inputcomponent__InputFieldInput-sc-x88sc3-3 cXOnMx")
        elem.send_keys("aaaaaaaaaaaaaaaa")
        elem.send_keys(RETURN)
        self.assertIn("endereço inválido") 
        driver.close()

    def CT_020():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "tel")
        elem.send_keys("$#@$#@$@#@")
        elem.send_keys(RETURN)
        self.assertIn("é necessário informar o número do telefone principal.") 
        driver.close()

    def CT_021():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "tel")
        elem.send_keys("aaaaaaaaaaaaaa")
        elem.send_keys(RETURN)
        self.assertIn("é necessário informar o número do telefone principal.") 
        driver.close()

    def CT_022():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "tel")
        elem.send_keys("100000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        elem.send_keys(RETURN)
        self.assertIn("é necessário informar o número do telefone principal.") 
        driver.close()

    def CT_023():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "tel")
        elem.send_keys("111-111-1111-1111-111")
        elem.send_keys(RETURN)
        self.assertIn("é necessário informar o número do telefone principal.") 
        driver.close()

    def CT_024():
        registrationLink = "https://cliente.americanas.com.br/minha-conta/cadastro?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.NAME, "tel")
        elem.send_keys("<script>alert(hello)</script>")
        elem.send_keys(RETURN)
        self.assertIn("hello") 
        driver.close()

class Search():
    def CT_025():
        registrationLink = "https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "search__InputUI-sc-1wvs0c1-2 dRQgOV")
        elem.send_keys("@@!@$#!$@#$")
        elem.send_keys(RETURN)
        self.assertIn("hello") 
        driver.close()

    def CT_026():
        registrationLink = "https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "search__InputUI-sc-1wvs0c1-2 dRQgOV")
        elem.send_keys("@@!@$#!$@#$")
        elem.send_keys(RETURN)
        self.assertIn("produto não encontrado") 
        driver.close()

    def CT_027():
        registrationLink = "https://cliente.americanas.com.br/simple-login/?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "entrar-inputUpperLink")
        elem2 = driver.find_element(By.CLASS_NAME, "form-control")
        elem.send_keys("ii")
        elem.send_keys(RETURN)
        self.assertIn("Please include an @ in the email adress") 
        driver.close()

    def CT_028():
        registrationLink = "https://cliente.americanas.com.br/simple-login/?next=https://www.americanas.com.br/"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "entrar-inputUpperLink")
        elem2 = driver.find_element(By.CLASS_NAME, "form-control")
        elem.send_keys("")
        elem.send_keys(RETURN)
        self.assertIn("Please include an @ in the email adress") 
        driver.close()

    def CT_029():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__InputQtyDescription-sc-11eb4gw-8 fToFUH")
        elem.send_keys("aaaaaaaaaaaaa")
        elem.send_keys(RETURN)
        driver.close()

    def CT_030():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__InputQtyDescription-sc-11eb4gw-8 fToFUH")
        elem.send_keys(2.2)
        elem.send_keys(RETURN)
        driver.close()

    def CT_031():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__InputQtyDescription-sc-11eb4gw-8 fToFUH")
        elem.send_keys(299999999999999)
        elem.send_keys(RETURN)
        self.assertIn("quantidade não disponivel") 
        driver.close()

    def CT_032():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__InputQtyDescription-sc-11eb4gw-8 fToFUH")
        elem.send_keys(-2)
        elem.send_keys(RETURN)
        self.assertIn("quantidade não disponivel") 
        driver.close()

    def CT_033():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcoupon-sc-12eb4w-8")
        elem.send_keys("")
        elem.send_keys(RETURN)
        self.assertIn("cupom inválido") 
        driver.close()

        
    def CT_034():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcoupon-sc-12eb4w-8")
        elem.send_keys("09/2060")
        elem.send_keys(RETURN)
        self.assertIn("data inválida") 
        driver.close()

                
    def CT_035():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcoupon-sc-12eb4w-8")
        elem.send_keys("00000000000000000000000000000000")
        elem.send_keys(RETURN)
        self.assertIn("número inválido") 
        driver.close()

    def CT_036():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcoupon-sc-12eb4w-8")
        elem.send_keys("dsafasfsdafasdf")
        elem.send_keys(RETURN)
        self.assertIn("this must be a number") 
        driver.close()

    def CT_037():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcoupon-sc-12eb4w-8")
        elem.send_keys("$%¨$%¨$%#¨%$¨#")
        elem.send_keys(RETURN)
        self.assertIn("número inválido") 
        driver.close()

    def CT_038():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcard-sc-12eb4w-8")
        elem.send_keys("")
        elem.send_keys(RETURN)
        self.assertIn("número inválido") 
        driver.close()

        
    def CT_039():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputname-sc-12eb4w-8")
        elem.send_keys(12131232)
        elem.send_keys(RETURN)
        self.assertIn("nome inválido") 
        driver.close()

    def CT_040():
        registrationLink = "https://www.americanas.com.br/produto/3079449571?pfm_carac=produtos%20mais%20vistos%20na%20americanas&pfm_index=2&pfm_page=home&pfm_pos=home_page.rr1&pfm_type=vit_recommendation&DCSext.recom=RR_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_origem=rec_home_page.rr1-mars_TopViews%3AF1%3A0%3Amars_ViewPurchasedUser%3Aads%3Dfalse%3AorderAdsTest%3Dmotor_control&nm_ranking_rec=2"
        driver.get(registrationLink)
        elem = driver.find_element(By.CLASS_NAME, "styles__Inputcard-sc-12eb4w-8")
        elem.send_keys("dsdadsfsf")
        elem.send_keys(RETURN)
        self.assertIn("número de cartão inválido") 
        driver.close()

