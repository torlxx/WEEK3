#Script_in_Python_per_simulazione_UDP_Flood

import socket      #modulo_sulle_socket
import random      #modulo_randon_per_generazione_byte_casuali 
SRV_ADDR = "192.168.33.100" #ip_client
SVR_PORT = 44444            #porta_client

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #nuovo_socket_con_parametri_per_IPv4_e_connessione_UDP
s.bind((SRV_ADDR , SRV_PORT)) #associazione_bind_indirizzo_e_porta_server
s.listen(1) #configurazione_socket_per_ascolto_IP:PORTA_indicati_e_numero_massimo_di_connessioni_in_coda
print ("Server started! Waiting for connection ...")
connection , address = s.accept() #metodo_accept_per_accettare_e_stabilre_connessione_con_il_client_restituendo_identificativo_connessione_e_IP_client
print ('Client connected with address: ' , address)
while 1: #scambio_dati_con_ciclo_while_infinito
    data = random.randbytes(1024) #utilizzato_per_ricevere_dati_client_random_a_1kb
    if not data: break
    connection.sedall (b'-- Message <received --\n')
    print (data.decode ('utf-8')) #stampa_a_video_pacchetti_dopo_decodifica_a_utf-8
connection.close() #chiusura_connessione
