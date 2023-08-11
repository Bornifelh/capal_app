import plotly as px
import pickle
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


mysql_config = {
    'host': "185.166.188.154",      # Adresse du serveur MySQL distant
    'user': 'u948053727_capal',  # Nom d'utilisateur MySQL
    'password': 'Decembre@2023',  # Mot de passe MySQL
    'database': 'u948053727_capal'   # Nom de la base de données à utiliser
}

#state des def a afficher --------------------------------------------


if 'show_register_user_content' not in st.session_state:
    st.session_state['show_register_user_content'] = False


if 'show_recapVenteGlaces_content' not in st.session_state:
    st.session_state['show_recapVenteGlaces_content'] = False

if 'show_vente_glaces_content' not in st.session_state:
    st.session_state['show_vente_glaces_content'] = False


if 'show_location_paiement_content' not in st.session_state:
    st.session_state['show_location_paiement_content'] = False

if 'show_location_verif_content' not in st.session_state:
    st.session_state['show_location_verif_content'] = False

if 'show_location_content' not in st.session_state:
    st.session_state['show_location_content'] = False

if 'show_transaction_content_views' not in st.session_state:
    st.session_state['show_transaction_content_views'] = False

if 'show_supprime_client_content' not in st.session_state:
    st.session_state['show_supprime_client_content'] = False


if 'show_dashboard_content' not in st.session_state:
    st.session_state['show_dashboard_content'] = False
    

if 'show_ajout_client' not in st.session_state:
    st.session_state['show_ajout_client'] = False


if 'show_transaction_content_views_depenses' not in st.session_state:
    st.session_state['show_transaction_content_views_depenses'] = False
    
if 'show_recap_transaction_ventes_content_view' not in st.session_state:
    st.session_state['show_recap_transaction_ventes_content_view'] = False



#------------------------------ Accueil et Menu ----------------------------------------#
def accueil_content():
    if st.session_state['loggedIn']:
        username = st.session_state['userName']
        st.sidebar.subheader(f"Bienvenue {username}")
        #barre de navigation
        
        with st.container():
                #---------------------------------------------------------------
            expanderTransactions = st.sidebar.expander("Transactions")
            with expanderTransactions:
                saisiCaisse_btn = expanderTransactions.button("Saisie de caisse")
                sortiCaisse_btn = expanderTransactions.button("Sortie de caisse")
                btn_tables_ventes = expanderTransactions.button("Recap des entrées caisse")
                btn_tablesDepenses = expanderTransactions.button("Recap des dépenses")
                    
                
                #---------------------------------------------------------------
                expanderGlaces = st.sidebar.expander("Vente glaces")
            with expanderGlaces:
                venteGlace_btn = expanderGlaces.button("Saisir une vente")
                recapVenteGlaces_btn = expanderGlaces.button("Visualisation des ventes")
                
                #---------------------------------------------------------------
            expanderPrincipal = st.sidebar.expander("Tableau de bord principal")
            with expanderPrincipal:
                    
                tabdeb_btn = expanderPrincipal.button("Tableau de bord de suivi")
                    
                #---------------------------------------------------------------
            expanderDebarquemet = st.sidebar.expander("Gestion des debarquements")
                
            with expanderDebarquemet:
                tabrecap_btn = expanderDebarquemet.button("Saisie des debarquements")
                
                #---------------------------------------------------------------
            expanderClient = st.sidebar.expander("Gestion des clients")
                
            with expanderClient:
                gestClient_btn = expanderClient.button("Ajouter un client")
                suppClient_btn = expanderClient.button("Supprimer un client")
                listClient_btn = expanderClient.button("Liste des clients")
                
                #---------------------------------------------------------------
            expander = st.sidebar.expander("Gestion des locations")
                    
            with expander:
                gestlocat_btn = expander.button("Nouvelle location")
                paiementLocation = expander.button("Saisir un paiement")
                listLocation = expander.button("Liste des locations")
                verifLocation = expander.button("Situation d'un locataire")
                
                #----------------------------------------------------------------
            expanderUtilisateur = st.sidebar.expander("Gestion des utilisateurs")
                
            with expanderUtilisateur:
                BtnListProfil = expanderUtilisateur.button("Liste des profiles")
                btnRegister = expanderUtilisateur.button("Créer un compte")
                
                
            # Afficher le contenu de la page sélectionnée
            if suppClient_btn:
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = True
                st.session_state['show_transaction_content_views_depenses'] = False
            
            
            if tabrecap_btn:
                st.session_state['show_dashboard_content'] = True
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                
            
            if gestlocat_btn:
                st.session_state['show_location_content'] = True
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                        
            if tabdeb_btn:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                tabdebarquement_content()
                        
            if gestClient_btn :
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_ajout_client'] = True
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                #gestion_client_content()
                        
            if btnRegister:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_register_user_content'] = True
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                
                            
            if BtnListProfil:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                list_client()
                        
            if listLocation:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                location_list()
                            
            if paiementLocation:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_paiement_content'] = True
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                        
            if verifLocation:
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_verif_content'] = True
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                
                
            if venteGlace_btn:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_vente_glaces_content'] = True
                st.session_state['show_register_user_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                #venteGlaces_content()
                
            if recapVenteGlaces_btn:
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = True
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                
                
                
            if saisiCaisse_btn:
                st.session_state['show_transaction_content_views'] = True
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                
            if sortiCaisse_btn:
                st.session_state['show_transaction_content_views_depenses'] = True
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False
                st.session_state['show_recap_transaction_ventes_content_view'] = False
                
            if btn_tables_ventes:
                st.session_state['show_recap_transaction_ventes_content_view'] = True
                st.session_state['show_transaction_content_views_depenses'] = False
                st.session_state['show_transaction_content_views'] = False
                st.session_state['show_ajout_client'] = False
                st.session_state['show_location_verif_content'] = False
                st.session_state['show_recapVenteGlaces_content'] = False
                st.session_state['show_vente_glaces_content'] = False
                st.session_state['show_register_user_content'] = False
                st.session_state['show_location_paiement_content'] = False
                st.session_state['show_location_content'] = False
                st.session_state['show_supprime_client_content'] = False
                st.session_state['show_dashboard_content'] = False


#------------------------------- Fin accueil et Menu -----------------------------------#






#----------------------------------------------------------------------

headerSection = st.container()
accueilSection  = st.container()
locationSection  = st.container()
tabdebarquementSection  = st.container()
loginSection = st.container()
registerSection = st.container()
dashboardSection = st.container()



def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input(label="", value="", placeholder="Saisissez votre compte")
            password = st.text_input(label="", value="", placeholder="Saisissez votre mot de passe", type='password')
            LoginBtnClicked = st.button("Se connecter")
            if LoginBtnClicked:
                if login_user(userName, password):
                    st.session_state['loggedIn'] = True
                else:
                    st.error("Utilisateur ou mot de passe Invalide")




#----------------- Interfaces gestion des clients -----------------#
ajoutClient = st.container() #ajout d'un client dans la bas de donnees
supprimerClient = st.container() #suppression d'un client dans la base de donnees

def ajout_client():
    if st.session_state['show_ajout_client']:
        with st.form(key='FormAddClient'):
            nomClient = st.text_input(label="", value="", placeholder="Saisissez le nom du client")
            prenomClient = st.text_input(label="", value="", placeholder="Saisissez le prénom du client")
            telClient = st.text_input(label="", value="", placeholder="Saisissez le téléphone du client")
            emailClient = st.text_input(label="", value="", placeholder="Saisissez l'E-mail du client")
            adresseClient = st.text_input(label="", value="", placeholder="Saisissez l'adresse du client")
            dateAjoutClient = st.date_input(label="Ajouté le")
            btnAjoutClient = st.form_submit_button("Ajouter le client")
ajout_client()
#-----------------------------------------------------------------#
        
        

def transaction_content_views():
    if st.session_state['show_transaction_content_views']:
        st.subheader("Saisie de caisse - entrée des fonds")
        with st.form(key='FormTransact'):
            venant_de = st.text_input(label="Provenance", value="", placeholder="Provenance des fonds")
            dateEncaissement = st.date_input(label="Date encaissement")
            detailsEncaissement = st.text_area(label="Details", value="", placeholder="Details sur la provenance des fonds")
            montantEncaissement = st.text_input(label="Montant", value="", placeholder="Montant réçu")
            
            btn_validation = st.form_submit_button("Valider")
transaction_content_views()


def transaction_content_views_depenses():
    if st.session_state['show_transaction_content_views_depenses']:
        st.subheader("Saisir une sortie de caisse")
        with st.form(key='FormTransactionSortie'):
            beneficiaire = st.text_input(label="Bénéficiaire", value="", placeholder="Saisir le Bénéficiaire")
            dateSortieCaisse = st.date_input(label="Date de saisie")
            detailSortieCaisse = st.text_area(label="Details", value="", placeholder="Saisir les details de la sortie de caisse")
            saisiPar = st.text_input(label="Montant", value="", placeholder="Montant de la dépense")
            
            btn_validation_sortie = st.form_submit_button("Valider")
transaction_content_views_depenses()


def recap_transaction_ventes_content_view():
    if st.session_state['show_recap_transaction_ventes_content_view']:
        st.subheader("Recap des transactions des entrées caisse")
recap_transaction_ventes_content_view()

sectionListClient = st.container()

def list_client():
    st.subheader('Liste des utilisateurs')
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    
    query = "SELECT userName, nom, prenom, phone, type, email FROM login"
    cursor.execute(query)
    
    data = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    column_titles = ["Nom d'utilisateur", "Nom", "Prénom", "Téléphone", "Type de compte", "E-mail"]
    
    df = pd.DataFrame(data, columns=column_titles)
    
    st.table(df)

def gestion_client_content():
    
    if st.session_state['show_supprime_client_content']:
        st.subheader("Supprimer un client")
        with st.form(key ='DeleteClient'):
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()
            
            query = "SELECT locataire FROM TabLocataire"
            cursor.execute(query)
            data = [item[0] for item in cursor.fetchall()]
            
            cursor.close()
            connection.close()
            nomDuClient = st.selectbox("Selectionnez le client a supprimer", data)
            btnDelete = st.form_submit_button("Supprimer")
            if btnDelete:
                connection = mysql.connector.connect(**mysql_config)
                cursor = connection.cursor()
                    
                queryDelete = "DELETE FROM TabLocataire WHERE locataire = %s"
                cursor.execute(queryDelete, (nomDuClient,))
                connection.commit()
                    
                cursor.close()
                connection.close()
                    
                st.success(f"Le client '{nomDuClient}' a été supprimé avec succès.")
gestion_client_content()

#------------------ fin gestion des clients ------------------------#


#------------------- Gestion des utilisateurs -----------------------#

def login_user(userName, password):
    try:
        connection = mysql.connector.connect(**mysql_config)
        
        cursor = connection.cursor()
        
        query = "SELECT password FROM login WHERE userName = %s;"
        cursor.execute(query, (userName,))
        result = cursor.fetchone()
        
        if result and len(result) > 0:
            hashed_password = result[0]
            if hashed_password == password:
                st.session_state['loggedIn'] = True
                st.session_state['userName'] = userName
                return True
        cursor.close()
        connection.close()
        
        return False
    except Exception as e:
        print(e)
        return False


def register_user(userNameRegister, password, FullName, FirstName, phone, typeLogin, email):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        
        insert_query_user = "INSERT INTO login(userName, password, nom, prenom, phone, type, email) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        
        values = (userNameRegister, password, FullName, FirstName, phone, typeLogin, email)
        
        cursor.execute(insert_query_user, values)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return True
    except Exception as e:
        print(e)
        return False
    
def table_exists(connection, TabLocataire):
    # Vérifie si une table existe dans la base de données
    cursor = connection.cursor()
    cursor.execute(f"SHOW TABLES LIKE '{TabLocataire}'")
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def create_table_if_not_exist(connection):
    # Crée la table TabLocataire si elle n'existe pas déjà
    create_table_query = """
    CREATE TABLE IF NOT EXISTS TabLocataire (
        id INT AUTO_INCREMENT PRIMARY KEY,
        locataire VARCHAR(255),
        numeroBox VARCHAR(255),
        montantLoc VARCHAR(255),
        dateEntree VARCHAR(255),
        typeBox VARCHAR(255),
        orderEditBy VARCHAR(255)
    );
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def nouveau_locataire(locataire, numeroBox, montantLoc, dateEntree, typeBox, orderEditBy):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        
        if not table_exists(connection, 'TabLocataire'):
            create_table_if_not_exist(connection)
        
        insert_query_locataire = "INSERT INTO TabLocataire(locataire, numeroBox, montantLoc, dateEntree, typeBox, orderEditBy) VALUES (%s, %s, %s, %s, %s, %s);"
        
        values = (locataire, numeroBox, montantLoc, dateEntree, typeBox, orderEditBy)
        
        cursor.execute(insert_query_locataire, values)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return True
    except Exception as e:
        print(e)
        return False






    
def register_user_content():
    if st.session_state['show_register_user_content']:
        with st.form(key ='RegisterUsers'):
            st.subheader("Créer un utilisateur")
            FullName = st.text_input(label="", value="", placeholder="Saisissez votre Nom")
            FirstName = st.text_input(label="", value="", placeholder="Saisissez le Prénom")
            userNameRegister = st.text_input(label="", value="", placeholder="Saisissez votre compte")
            password = st.text_input(label="", value="", placeholder="Saisissez votre mot de passe" ,type='password')
            passwordConfirme = st.text_input(label="", value="", placeholder="Confirmer votre mot de passe" ,type='password')
            phone = st.text_input(label="", value="", placeholder="Saisissez votre numéro de téléphone", type='default')
            typeLogin = st.selectbox("Type d'utilisateur", ("Administrateur","Responsable", "Utilisateur"))
            email = st.text_input(label="", value="", placeholder="Saisissez votre E-mail", type='default')
            RegisterLoginBtn = st.form_submit_button("Enregistrer le compte")
            if RegisterLoginBtn:
                if password == passwordConfirme:
                    if register_user(userNameRegister, password, FullName, FirstName, phone, typeLogin, email):
                        st.success("Compte enregistré avec succés")
                        st.session_state['show_register_user_content'] = False
                        FullName = ""
                        FirstName = ""
                        userNameRegister = ""
                        password = ""
                        passwordConfirme = ""
                        phone = ""
                        typeLogin = ""
                        email = ""
                    else:
                        st.error("Impossible d'enregistrer les donnees")
                else:
                    st.error('Les mots de passe ne correspondent pas.')
register_user_content()

#---------------------------------- Fin gestion des utilisateurs -----------------------#

#---------------------------------- Gestion des ventes glaces --------------------------#



def table_vtGlace_exists(connection, Glaces):
    cursor = connection.cursor()
    cursor.execute(f"SHOW TABLES LIKE '{Glaces}'")
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def create_table_if_not_exist_glaces(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Glaces (
        id INT AUTO_INCREMENT PRIMARY KEY,
        clientSelect VARCHAR(255),
        TypeSacGlace VARCHAR(255),
        nbSacGlace VARCHAR(255),
        dateVenteGlace VARCHAR(255),
        montantVenteGlace VARCHAR(255),
        orderEditBy VARCHAR(255)
    );
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def nouveau_vtGlace(clientSelect, TypeSacGlace, nbSacGlace, dateVenteGlace, montantVenteGlace, orderEditBy):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        
        if not table_exists(connection, 'Glaces'):
            create_table_if_not_exist_glaces(connection)
        
        insert_query_glaces = "INSERT INTO Glaces(clientSelect, TypeSacGlace, nbSacGlace, dateVenteGlace, montantVenteGlace, orderEditBy) VALUES (%s, %s, %s, %s, %s, %s);"
        
        values = (clientSelect, TypeSacGlace, nbSacGlace, dateVenteGlace, montantVenteGlace, orderEditBy)
        
        cursor.execute(insert_query_glaces, values)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return True
    except Exception as e:
        print(e)
        return False



def table_payementLoc_exists(connection, PayementLoc):
    # Vérifie si une table existe dans la base de données
    cursor = connection.cursor()
    cursor.execute(f"SHOW TABLES LIKE '{PayementLoc}'")
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def create_table_if_not_exist_payementLoc(connection):
    # Crée la table TabLocataire si elle n'existe pas déjà
    create_paiement_query = """
    CREATE TABLE IF NOT EXISTS PayementLoc (
        id INT AUTO_INCREMENT PRIMARY KEY,
        NomClient VARCHAR(255),
        PeriodePayement VARCHAR(255),
        TypeLocation VARCHAR(255),
        NumeroBox VARCHAR(255),
        montantPaiement VARCHAR(255),
        DatePaiement VARCHAR(255),
        paye VARCHAR(255),
        saisiPar VARCHAR(255)
    );
    """
    cursor = connection.cursor()
    cursor.execute(create_paiement_query)
    connection.commit()
    cursor.close()

def nouveau_PaiementLoc(NomClient, PeriodePayement, TypeLocation, NumeroBox, montantPaiement, DatePaiement, paye, saisiPar):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        
        if not table_exists(connection, 'PayementLoc'):
            create_table_if_not_exist_payementLoc(connection)
        
        insert_query_PayementLoc = "INSERT INTO PayementLoc(NomClient, PeriodePayement, TypeLocation, NumeroBox, montantPaiement, DatePaiement, paye, saisiPar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        
        values = (NomClient, PeriodePayement, TypeLocation, NumeroBox, montantPaiement, DatePaiement, paye, saisiPar)
        
        cursor.execute(insert_query_PayementLoc, values)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return True
    except Exception as e:
        print(e)
        return False



def venteGlaces_content():
    if st.session_state['show_vente_glaces_content']:
        #form_key = f"FormVenteGlace_{int(time.time() * 1000)}"
        with st.form(key='FormVenteGlace'):
            st.subheader("Vente des glaces")
            clientSelect = st.selectbox("Client ",("CAPAL - Box","Vendeur(se) en table","Tiers payant"))
            TypeSacGlace = st.selectbox("Type de sac", ("Grand sac", "Sac moyen", "Sachet de 100F"))
            nbSacGlace = st.text_input(label="", value="", placeholder="Nombre de sac")
            dateVenteGlace = st.date_input(label="Date de vente")
            montantVenteGlace = st.text_input(label="", value="", placeholder="Montant de la vente")
            orderEditBy = st.text_input(label="", value="", placeholder="Vente effectuée par")
            validVenteGlace_btn = st.form_submit_button("Enregistrer la vente")
            if validVenteGlace_btn:
                if nouveau_vtGlace(clientSelect, TypeSacGlace, nbSacGlace, dateVenteGlace, montantVenteGlace, orderEditBy):
                    st.success("Paiement effectué")
                    # Masquer le contenu après avoir appuyé sur le bouton
                    st.session_state['show_vente_glaces_content'] = False
venteGlaces_content()



def recapVenteGlaces_content(): #Tableau de vente des glaces
    if st.session_state['show_recapVenteGlaces_content']:
        
        st.subheader("Suivi de vente des glaces")
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        
        query = "SELECT clientSelect, TypeSacGlace, nbSacGlace, dateVenteGlace, montantVenteGlace, orderEditBy FROM Glaces"
        cursor.execute(query)
        
        data = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        column_titles = ["Client","Type de sac", "Nombre de sac", "Date de vente", "Montant","Vendu par"]
        
        df = pd.DataFrame(data, columns=column_titles)
        
        st.table(df)
        
recapVenteGlaces_content()
    
#---------------------------------- Fin gestion des glaces -----------------------------#




#------------------------------- Gestion locations ---------------------------------------#


def location_paiement_content(): #Saisi des paiements de locations
    if st.session_state['show_location_paiement_content']:
        st.subheader("Paiement des locations")
        with st.form(key='PaiementLocation'):
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()
            
            
            
            query = "SELECT locataire FROM TabLocataire"
            cursor.execute(query)
            data = [item[0] for item in cursor.fetchall()]
            
            NomClient = st.selectbox("Liste des locataires", data)
            
            PeriodePayement = st.selectbox("Période à payer", ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre"))
            TypeLocation = st.selectbox("Tybe de box ou espace", ("Box", "Espaces vente au detail", "Comptoir decaillage", "Espace vert(containers)", "Espace quai", "Gardienage des bateaux de plaisance", "Cases des pêcheurs", "Espace vente produits connexe à la pêche", "Salle de transformation", "Toilettes"))
            NumeroBox = st.text_input(label="", value="", placeholder="Numéro de box")
            montantPaiement = st.text_input(label="", value="", placeholder="Montant à payer")
            DatePaiement = st.date_input(label="Date paiement")
            paye = st.selectbox("", ("Payé","Avance"))
            saisiPar = st.text_input(label="", value="", placeholder="Saisi par")
            
            orderLocationBtn = st.form_submit_button("Valider le paiement")
            if orderLocationBtn:
                if nouveau_PaiementLoc(NomClient, PeriodePayement, TypeLocation, NumeroBox, montantPaiement, DatePaiement, paye, saisiPar):
                    st.success("Saiaie du paiement effectué avec succés")
                else:
                    st.error("Impossible d'effectuer le paiement, merci de verifier votre connexion")
location_paiement_content()

def location_verif_content(): #verification de l'etat d'un client
    if st.session_state['show_location_verif_content']:
        st.subheader("Situation d'un locataire")
        with st.form(key='VerifLoc'):
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()
            
            query = "SELECT locataire FROM TabLocataire"
            cursor.execute(query)
            data = [item[0] for item in cursor.fetchall()]
            
            cursor.close()
            connection.close()
            nomLocataire = st.selectbox("Liste des locataires", data)
            verifLocBtn = st.form_submit_button("Vérifier")
            if verifLocBtn:
                connection = mysql.connector.connect(**mysql_config)
                cursor = connection.cursor()
                
                query = "SELECT * FROM PayementLoc WHERE NomClient LIKE %s"
                cursor.execute(query, ('%' + nomLocataire + '%',))
                data = cursor.fetchall()
                
                cursor.close()
                connection.close()
                
                if data:
                    df = pd.DataFrame(data, columns=["ID", "NomClient", "PeriodePayement", "TypeLocation","NumeroBox", "montantPaiement", "DatePaiement", "Payé", "saisiPar"])  # Remplacez "AutresColonnes" par les noms réels des colonnes
                    st.dataframe(df)
                else:
                    st.write("Aucune information trouvée pour la rubrique spécifiée.")
location_verif_content()


def location_content(): #saisi des location (debut de location)
    if st.session_state['show_location_content']:
        if st.session_state['loggedIn']:
            username = st.session_state['userName']
            with st.form(key ='FormLocation'):
                st.subheader("Nouvelle location")
                locataire = st.text_input(label="", value="", placeholder="Locataire")
                numeroBox = st.text_input(label="", value="", placeholder="Numero de Box ou place de vente")
                montantLoc = st.text_input(label="", value="", placeholder="Montant de la location par Mois")
                dateEntree = st.date_input(label="Date d'entrée")
                typeBox = st.selectbox("Tybe de box ou espace", ("Box", "Espaces vente au detail", "Comptoir decaillage", "Espace vert(containers)", "Espace quai", "Gardienage des bateaux de plaisance", "Cases des pêcheurs", "Espace vente produits connexe à la pêche", "Salle de transformation", "Toilettes"))
                orderEditBy = st.text_input(label="", value=f"{username}", placeholder="Reçu par")
                LocBtnNew = st.form_submit_button("Enregistrer")
                if LocBtnNew:
                    if nouveau_locataire(locataire, numeroBox, montantLoc, dateEntree, typeBox, orderEditBy):
                        locataire = ""
                        numeroBox = ""
                        montantLoc = ""
                        dateEntree = ""
                        typeBox = ""
                        orderEditBy = ""
                        st.success("Locataire ajouté")
                    else:
                        st.error("Impossible d'ajouter le locataire")
                    
location_content()


def location_list(): #liste des locations actuelles
    st.subheader("Liste des locataires")
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    
    query = "SELECT locataire, numeroBox, montantLoc, dateEntree, typeBox FROM TabLocataire"
    cursor.execute(query)
    
    data = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    column_titles = ["Nom du locataire","Numero de box", "Montant", "Date d'entrée", "Type de boxe(Espaces)"]
    
    df = pd.DataFrame(data, columns=column_titles)
    
    st.table(df)

#-------------------------------- Fin gestion locations -----------------------------------#



#----------------------------------------------- Gestion debarquements ---------------------------------------#
def tabdebarquement_content():
    st.title("Tableau de bord de suivi")
    st.subheader("Table des transactions")
    
    dtf = pd.read_csv("capal_dfc.csv", sep=';')
    pdFrame = pd.DataFrame(dtf)
    st.dataframe(pdFrame)

    # Somme des montants payés par mois
    montants_par_mois = dtf[['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
                            'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']].sum()

    # Créer le graphique à secteurs
    fig, ax = plt.subplots(figsize=(8, 8))
    pie = ax.pie(montants_par_mois, labels=montants_par_mois.index, autopct='%1.1f%%', startangle=90)
    
    #afficher legenge
    ax.legend(pie[0], montants_par_mois.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    # Ajouter un titre
    ax.set_title('Répartition des montants payés par mois')

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)



def dashboard_content():
    if st.session_state['show_dashboard_content']:
        
            st.subheader("Debarquement - saisie des donnees")
            
            #method de saisie des donnees - Debarquement
            with st.form(key ='Form1'):
                dateDebarquement = st.date_input(label="Date debarquement", format="DD/MM/YYYY")
                siteDebarquement = st.text_input(label="Site debarquement")
                nomPirogue= st.text_input(label="Nom pirogue")
                immatPirogue= st.text_input(label="Immatricualtion pirogue")
                Pirogue= st.text_input(label="Pirogue") #inclut le nom de la pirogue et le l'immatriculation
                cooperative = st.text_input(label="Cooperative")
                engin = st.text_input(label="Engin")
                zonepeche = st.text_input(label="Zone de peche")
                zonedattache = st.text_input(label="Zone d'attache")
                frequentations = st.text_input(label="Frequentations")
                dureemaree = st.text_input(label="Duree maree")
                numAuto = st.number_input(label="Numero automatique", min_value=0, step=1)
                typeMaree= st.text_input(label="Type de maree")
                
                annee = st.date_input("Annees encours")
                
                mois = st.selectbox("Mois", 
                                        ('Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre'))
                
                
                #listing des elements peche
                
                #options = st.multiselect('Choix des produits', ['Capitaine', 'Bars','Bossu', 'Becume' ,'Daurade', 'Machoiron', 'Sole','Rouge','Carpe de mer'])
                st.subheader("ELEMENTS PECHES")
                options = ['Capitaine', 'Bars', 'Bossu', 'Becune', 'Daurade', 'Machoiron', 'Sole', 'Rouge', 'Carpe de mer']
                
                df = pd.DataFrame(columns=["Elements", "Quantite"])
                
                options_selected = st.multiselect('Choix des produits', options)
                
                submit_button = st.form_submit_button("Attribuer les quantités")
                
                if submit_button:
                    quantites = {}
                    for option in options_selected:
                        quantite = st.text_input(f"Quantité pour {option}", value="")
                        quantites[option] = quantite
                    
                    
                    df = pd.DataFrame({"Elements": list(quantites.keys()), "Quantite": str(quantites.values())})
                st.subheader("Autres informations")
                
                
                
                
                
                
                cpueKgJr = st.text_input(label="CPUE (kg/jr)")
                taxeDemers = st.text_input(label="Taxe démers.")
                taxePelagi = st.text_input(label="Taxe pélagi.")
                taxeSardine = st.text_input(label="Taxe sardine")
                taxeCrust = st.text_input(label="Taxe Crust.")
                totalTaxe = st.text_input(label="Total taxe (F CFA)")
                    
                    
                dureeEmbarcation = st.number_input(label="Durée de pêche par embarcations (jrs)", min_value=0, step=1)
                natProprioPirogue = st.selectbox("Nationalité du propriétaire de la pirogue", ('Åland(les Îles)','Albanie','Algérie','Allemagne','Andorre','Angola','Anguilla','Antarctique','Antigua-et-Barbuda','Arabie saoudite','Argentine','Arménie','Aruba','Australie','Autriche','Azerbaïdjan','Bahamas','Bahreïn','Bangladesh','Barbade','Bélarus','Belgique','Belize','Bénin','Bermudes','Bhoutan','Bolivie','Bonaire, Saint-Eustache et Saba','Bosnie-Herzégovine','Botswana','Bouvet (l’Île)','Brésil','Brunéi Darussalam','Bulgarie','Burkina Faso','Burundi','Cabo Verde','Caïmans (les Îles)','Cambodge','Cameroun','Canada','Chili','Chine','Christmas (l’Île)','Chypre','Cocos (les Îles) / Keeling (les Îles)','Colombie','Comores','Congo','Congo (RDC)','Cook (les Îles)','Corée','Corée du Nord','Costa Rica','Côte d’Ivoire','Croatie','Cuba','Curaçao','Danemark','Djibouti','République dominicaine','Dominique','Égypte','El Salvador','Émirats arabes unis','Équateur','Érythrée','Espagne','Estonie','Eswatini','États-Unis d’Amérique','Éthiopie','Malouines (les Îles)','Féroé (les Îles)','Fidji','Finlande','France','Gabon','Gambie','Géorgie','Géorgie du Sud – Îles Sandwich du S.','Ghana','Gibraltar','Grèce','Grenade','Groenland','Guadeloupe','Guam','Guatemala','Guernesey','Guinée','Guinée équatoriale','Guinée-Bissau','Guyana','Guyane française (la )','Haïti','Heard-et-Îles MacDonald (l’Île)','Honduras','Hong Kong','Hongrie','Île de Man','Îles mineures éloignées des États-Unis','Inde','Indonésie','Iran','Iraq','Irlande','Islande','Israël','Italie','Jamaïque','Japon','Jersey','Jordanie','Kazakhstan','Kenya','Kirghizistan','Kiribati','Koweït','Laos','Lesotho','Lettonie','Liban','Libéria','Libye','Liechtenstein','Lituanie','Luxembourg','Macao','Macédoine du Nord','Madagascar','Malaisie','Malawi','Maldives','Mali','Malte','Mariannes du Nord (les Îles)','Maroc','Marshall (les Îles)','Martinique','Maurice','Mauritanie','Mayotte','Mexique','Micronésie (États fédérés)','Moldavie','Monaco','Mongolie','Monténégro','Montserrat','Mozambique','Myanmar','Namibie','Nauru','Népal','Nicaragua','Niger','Nigéria','Niue','Norfolk (l’Île)','Norvège','Nouvelle-Calédonie','Nouvelle-Zélande','Oman','Ouganda','Ouzbékistan','Pakistan','Palaos','Palestine, État de','Panama','Papouasie-Nouvelle-Guinée','Paraguay','Pays-Bas','Pérou','Philippines','Pitcairn','Pologne','Polynésie française','Porto Rico','Portugal','Qatar','République arabe syrienne','République centrAfriqueine','Réunion','Roumanie','Royaume-Uni','Russie (la Fédération de)','Rwanda','Sahara occidental','Saint-Barthélemy','Sainte-Hélène, Ascension et Tristan da Cunha','Sainte-Lucie','Saint-Kitts-et-Nevis','Saint-Marin','Saint-Martin (partie française)','Saint-Martin (partie néerlandaise)','Saint-Pierre-et-Miquelon','Saint-Siège','Saint-Vincent-et-les Grenadines','Salomon (les Îles)','Samoa','Samoa américaines','Sao Tomé-et-Principe','Sénégal','Serbie','Seychelles','Sierra Leone','Singapour','Slovaquie','Slovénie','Somalie','Soudan','Soudan du Sud','Sri Lanka','Suède','Suisse','Suriname','Svalbard et l’Île Jan Mayen','Tadjikistan','Taïwan (Province de Chine)','Tanzanie (la République-Unie de)','Tchad','Tchéquie','Terres australes françaises','Thaïlande','Timor-Leste','Togo','Tokelau','Tonga','Trinité-et-Tobago','Tunisie','Turkménistan','Turks-et-Caïcos (les Îles)','Turquie','Tuvalu','Ukraine','Uruguay','Vanuatu','Venezuela','Vierges britanniques (les Îles)','Vierges des États-Unis (les Îles)','Viet Nam','Wallis-et-Futuna','Yémen','Zambie','Zimbabwe'))
                erreurConstat = st.selectbox("Erreur constatée lors de la saisie ? (Oui / Non)", ('Oui','Non'))
                totalCapture2 = st.number_input(label="Total capture2", min_value=0, step=1)
                dureePecheParEmbarquations = st.number_input(label="Durée de pêche par embarcations (jrs)3", min_value=0, step=1)
                nbrEnregJour = st.number_input(label="Nombre d'enregistrements de captures par jour", min_value=0, step=1)
                poidsPJ = st.number_input(label="Poids pêché par jour", min_value=0, step=1)
                totalDureeMerJr = st.number_input(label="Total des durées de marées par jour", min_value=0, step=1)
                
                
                submit_button = st.form_submit_button("Enregistrer")
                if submit_button:
                    st.success("Donnees enregistrees avec succes")
dashboard_content()
#------------------------------------------------ Fin debarquements --------------------------------------------#

#------------------------- "Tableau de bord" ----------------------------#







#-------------------------------- Logon --------------------------------#
with headerSection:
    st.title("CAPAL APP")
    
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page()
    else:
        if st.session_state['loggedIn']:
            accueil_content()
        else:
            show_login_page()
            






#--------------------------------Fin logon -----------------------------#



